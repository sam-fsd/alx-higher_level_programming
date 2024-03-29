#!/usr/bin/python3
"""Prints error code greater than 400"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
