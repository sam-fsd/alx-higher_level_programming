#!/usr/bin/python3
"""GET request with urllib"""

import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as res:
        body = res.read()

        print('Body response:')
        print(f'    - type: {type(body)}')
        print(f'    - content: {body}')
        print(f'    - utf8 content: {body.decode("utf-8")}')
