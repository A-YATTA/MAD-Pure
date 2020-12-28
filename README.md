# Mass Apk Download - Pure

`MAD-Pure` is a multithreaded Python script that download a list of APKs from [APKPure](https://apkpure.com/) and analyze them using androguard and pwnlibs.

## Requirements
`AMD-Pure` is written in Python 3 (and therefore **requires a minimum of `Python 3.6`**) in addition to the following libraries:
- requests
- bs4
- androguard 
- pwnlibs

## Malware detection
- wolfrat
- anubis
- actionSpy


## Usage
```
usage: mad-pure.py [-h] [-f FILE_LIST_APKS] [-o OUT_DIR] [-a AAPT_PATH] [-t NB_THREADS]

MDMA-Pure

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_LIST_APKS, --file FILE_LIST_APKS
                        File with applications name
  -o OUT_DIR, --out-dir OUT_DIR
                        Directory where apks will be stored
  -a AAPT_PATH, --aapt2-path AAPT_PATH
                        Path of aapt2 binary
  -t NB_THREADS, --threads NB_THREADS
                        Number of threads to use
```
If aapt2 is in you PATH env var you don't have to specify it, by default the program will look in PATH var.
out_dir is the output directory. by default: temp


## Support 

[![Coffee](https://img.buymeacoffee.com/button-api/?text=Support&emoji=&slug=secthetech&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/secthetech)
[![Patreon](https://img.shields.io/badge/patreon-donate-blue.svg)](https://www.patreon.com/secthetech)