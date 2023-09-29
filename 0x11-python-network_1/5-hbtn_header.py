#!/usr/bin/python3
""" script that takes in URL, sends a request to
    URL and displays value of variable X-Request-Id
    in response header
"""
import sys
import requests

if __name__ == "__main__":
    req_res = requests.get(sys.argv[1])
    print(req_res.headers.get("X-Request-Id"))
