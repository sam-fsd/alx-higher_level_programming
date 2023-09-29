#!/usr/bin/python3
"""POST request with requests library"""

import requests
from sys import argv


if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(type(r.text))
