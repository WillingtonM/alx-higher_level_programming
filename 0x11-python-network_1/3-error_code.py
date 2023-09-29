#!/usr/bin/python3
""" Sends request to URL & displays the body of response decoded in uft-8)
"""
from sys import argv
import urllib.error as error
import urllib.request as req
import urllib.parse as parse

if __name__ == "__main__":
    url = argv[1]

    url_req = req.Request(url)
    try:
        with req.urlopen(url_req) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
