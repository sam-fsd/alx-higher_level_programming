#!/usr/bin/python3
"""Getting header variable from url response"""

import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    r_headers = r.headers
    print(r_headers['X-Request-Id'])
