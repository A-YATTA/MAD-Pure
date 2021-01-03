from subprocess import run, PIPE
import re

def check_header(header):
    if header == "504b0304":
        return "JAR"

    if header == "7f454c46":
        return "ELF"

    return "UNKNOWN"


class APKUtils:

    def __init__(self, aapt_path):
        self.aapt_path = aapt_path

    """
    https://developer.android.com/studio/command-line/aapt2

    "command" argument can be one of: 
        apc 	        Print the contents of the AAPT2 Container (APC) generated during compilation.
        badging *	    Print information extracted from the APK's manifest.
        configurations 	Print every configuration used by a resource in the APK.
        packagename 	Print the APK's package name.
        permissions *	Print the permissions extracted from the APK's manifest.
        strings 	    Print the contents of the APK's resource table string pool.
        styleparents 	Print the parents of styles used in the APK.
        resources 	    Print the contents of the APK's resource table.
        xmlstrings 	    Print strings from the APK's compiled xml.
        xmltree 	    Print a tree of the APK's compiled xml. 
    """

    def aapt_dump_apk(self, command, apk_path):
        try:
            result = run([
                self.aapt_path, 'dump', command, apk_path],
                stdout=PIPE, stderr=PIPE, check=True,
                universal_newlines=True)
            return result.stdout
        except Exception as e:
            print(e)

        return ""

    """
    "aaptPermissionOutput" is the output of the command "aapt dump permissions my-app.apk" else it will fail
    """

    @staticmethod
    def get_app_package_version(aapt_output):
        return aapt_output.split("versionName='")[1].split("'")[0]

    """
    "aaptPermissionOutput" is the output of the command "aapt dump permissions my-app.apk" else it will fail
    """

    @staticmethod
    def get_app_package_name(aapt_output):
        output = aapt_output.split("\n")[0].split(":'")[1]
        print(output)
        if len(output) > 0:
            return output[0]

        return ""

    @staticmethod
    def get_permissions(aapt_permission_output):
        permissions = []
        for line in aapt_permission_output.split("\n"):
            if re.search("^uses-permission", line):

                permissions.append((line.split("'")[1]).strip())

        return permissions

    @staticmethod
    def get_supported_architectures(aapt_badging_output):
        supported_arch = []
        for line in aapt_badging_output.split("\n"):
            if re.search("^native-code", line):
                supported_arch_output = (line.split(":")[1]).strip()
                supported_arch = supported_arch_output.replace("'", "").split(" ")

        return supported_arch
