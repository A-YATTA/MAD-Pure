# Mass Apk Download - Pure

`MAD-Pure` is a multi-threaded Python script that download a list of APKs from [APKPure](https://apkpure.com/) and analyze them using androguard and pwnlibs.

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

## Tests
Tested on Linux 

## Contribution
If you have any idea how to improve this tool please create an issue or send a pull request.