import requests
from bs4 import BeautifulSoup
import sys
import mmap
import os
import re
import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from apkutils import APKUtils
from androhelper import AndroHelper

DEBUG = False
URL = "https://apkpure.com"

out_dir = "temp"
file_list_apks = "apps_names_example.txt"
aapt_path = "aapt2"
nb_threads = 4


def download_apk(url, filename):
    req = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(req.content)


def search_dl_app(app_name, output_file):

    search_url = "https://apkpure.com/search?q={}&t=app".format(app_name)
    req = requests.get(search_url)

    # Check status code
    if req.status_code != 200:
        print("Error Occurred while processing {}".format(
            app_name), file=sys.stderr)
        sys.exit(-1)

    soup = BeautifulSoup(req.text, 'html.parser')

    path = soup.find_all('dl')[0].a["href"]

    url_app = URL + path + "/download?from=details"

    if DEBUG:
        print("[DEBUG] URL APP: " + url_app)

    # Follow redirect to download APK page
    req = requests.get(url_app, allow_redirects=True)

    soup = BeautifulSoup(req.text, 'html.parser')

    download_link = soup.findAll(id="download_link")[0]["href"]

    if DEBUG:
        print("[DEBUG] DOWNLOAD LINK: " + download_link)

    download_apk(download_link, out_dir + "/" + output_file)
    dump_info(aapt_path, out_dir + "/" + output_file)


def process(file_apps_name, out_directory, nb_threads):
    if not os.path.isdir(out_directory):
        try:
            os.makedirs(out_directory)
        except OSError as e:
            print(e)

    with open(file_apps_name, "r+") as f:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        lines = m.read().decode("utf-8").strip().split("\n")

    with ThreadPoolExecutor(max_workers=nb_threads) as executor:
        results = {executor.submit(search_dl_app, re.sub('\W+', ' ', app_name), re.sub('\W+', ' ', app_name) +".apk"):
                        app_name for app_name in lines}
        for res in as_completed(results):
            print(res.result())


def dump_info(aapt_path, apk_path):
    info = {}

    apk_utils = APKUtils(aapt_path)
    output_permissions = apk_utils.aapt_dump_apk("permissions", apk_path)
    info["permissions"] = APKUtils.get_permissions(output_permissions)

    andro_helper = AndroHelper(apk_path, apk_path+".out")
    info["malware"] = andro_helper.analyze()

    if len(info["malware"]["packed_file"]):
        print("WARNING: %s contains packed apk(s)" % apk_path)

    for malware, found in info["malware"]["detected_malware"].items():
        if found > 0:
            print("ALERT: %s is probably a %s" % (apk_path, malware))

    with open(apk_path+".out/report.json", 'w') as file:
        file.write(json.dumps(info, indent=4, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MDMA-Pure",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f', '--file', dest="file_list_apks",
                        help='File with applications name', default=file_list_apks)

    parser.add_argument('-o', '--out-dir', dest="out_dir",
                        help='Directory where apks will be stored', default=out_dir)

    parser.add_argument('-a', '--aapt2-path', dest="aapt_path",
                        help='Path of aapt2 binary')

    parser.add_argument('-t', '--threads', dest="nb_threads",
                        help='Number of threads to use')

    args = parser.parse_args()

    if args.file_list_apks:
        file_list_apks = args.file_list_apks

    if not os.path.isfile(file_list_apks):
        print("File %s does not exist." % file_list_apks)
        exit(-1)

    if args.out_dir:
        out_dir = args.out_dir

    if args.aapt_path:
        aapt_path = args.aapt_path

    if args.nb_threads:
        nb_threads = int(args.nb_threads)

    process(file_list_apks, out_dir, nb_threads)
