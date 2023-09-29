#!/usr/bin/python3
""" 
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    req_res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req_res.text)))
    print("\t- content: {}".format(req_res.text))
