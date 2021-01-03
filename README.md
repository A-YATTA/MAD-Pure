# Mass Apk Download - Pure

`MAD-Pure` is a multithreaded Python script that download a list of APKs from [APKPure](https://apkpure.com/) and analyze them using androguard and pwnlibs.

## Requirements
`MAD-Pure` is written in Python 3 (and therefore **requires a minimum of `Python 3.6`**) in addition to the following libraries:
- requests
- bs4
- androguard 
- pwntools

## Malware detection
- wolfrat
- anubis
- actionSpy

## Install requirements
```
python3 -m venv mad
source mad/bin/activate
(mad)$ pip install -r requirements.txt
```
## Usage
```
usage: mad-pure.py [-h] [-f FILE_LIST_APKS] [-o OUT_DIR] [-a AAPT_PATH] [-t NB_THREADS]

MAD-Pure

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_LIST_APKS, --file FILE_LIST_APKS
                        File with applications name. Default: apps_names_example.txt
  -o OUT_DIR, --out-dir OUT_DIR
                        Directory where apks will be stored. Default: temp
  -a AAPT_PATH, --aapt2-path AAPT_PATH
                        Path of aapt2 binary. Default: check the PATH env
  -t NB_THREADS, --threads NB_THREADS
                        Number of threads to use, value between 1 and 8. Default: 4
```
If aapt2 is in your PATH env var you don't have to specify it, by default the script will look in PATH var.

OUT_DIR is the output directory, by default: temp

Please consider using a small NB_THREADS to do not impact the availability of APKPure, also a big number of threads will 
slow down the computer as Androguard and pwntools can be resource intensive depending on the APK to analyze.

## Tests
Tested on Linux only 

## Participation
If you have any idea how to improve this tool please create an issue or send a pull request.

If any malware or suspicious application is detected:
 - create an issue with the name of the application and it will be analyzed and a profile will be created to detect it
 - send a pull request for a new malware profile

## Support 
[![Coffee](https://img.buymeacoffee.com/button-api/?text=Support&emoji=&slug=secthetech&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/secthetech)
[![Patreon](https://img.shields.io/badge/patreon-donate-blue.svg)](https://www.patreon.com/secthetech)