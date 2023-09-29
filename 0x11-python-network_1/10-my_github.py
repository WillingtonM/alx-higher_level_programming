#!/usr/bin/python3
"""get thy properties from mail"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    req_auth = HTTPBasicAuth(argv[1], argv[2])
    req_res = requests.get("https://api.github.com/user", auth=req_auth)

    print(req_res.json().get("id"))
