#!/usr/bin/python
"""Script for cleaning subs from HTML tags.
"""
__author__ = "Pavel Py"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Pavel Py"
__email__ = "pavel.py3@gmail.com"

import os
import sys

if sys.version_info[:2] < (3, 5):
    raise Exception("Must be using Python 3.5+")
import glob

# 3rd party packages
from bs4 import BeautifulSoup


def clear_text(text):
    if text.strip():
        soup = BeautifulSoup(text, features="lxml")
        result = soup.get_text()
    else:
        result = text
    return result


def main():
    search_dir = None
    if len(sys.argv) > 1:
        search_dir = sys.argv[0]
        search_dir = search_dir if os.path.isdir(search_dir) else None
    search_dir = search_dir or os.getcwd()

    search_mask = os.path.join(search_dir, '**/*.srt')
    for filename in glob.iglob(search_mask, recursive=True):
        filecontent = []
        with open(filename, mode='r') as f:
            for line in (clear_text(l) for l in f):
                filecontent.append(line)
        with open(filename, mode='w') as f:
            f.writelines(filecontent)


if __name__ == '__main__':
    main()
