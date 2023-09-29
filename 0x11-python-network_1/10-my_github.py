#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    api_url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(argv[1], argv[2])
    headers = {
        'Accept': 'application/vnd.github+json',
    }

    r = requests.get(api_url, headers=headers, auth=auth)
    print(r.json())
