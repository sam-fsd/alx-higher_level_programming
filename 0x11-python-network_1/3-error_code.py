#!/usr/bin/python3
"""Handling HTTP error"""

import urllib.request
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    req = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(req) as res:
            html = res.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
