#!/usr/bin/python3
"""Getting header variable from url response"""

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    r_headers = r.headers
    print(r_headers['X-Request-Id'])
