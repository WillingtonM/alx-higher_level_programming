#!/usr/bin/python3
""" Sends request to given URL & display body of response."""

from sys import argv
import requests

if __name__ == "__main__":
    req_url = argv[1]

    req_res = requests.get(req_url)
    if req_res.status_code >= 400:
        print("Error code: {}".format(req_res.status_code))
    else:
        print(req_res.text)
