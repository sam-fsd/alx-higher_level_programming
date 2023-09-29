#!/usr/bin/python3
"""POST request with urllib"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
