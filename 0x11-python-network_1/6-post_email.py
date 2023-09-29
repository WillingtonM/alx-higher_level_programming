#!/usr/bin/python3
"""POST email using requests"""
import sys
import requests

if __name__ == "__main__":

    dta = {'email': sys.argv[2]}
    req_res = requests.post(sys.argv[1], dta=dta)
    print(req_res.text)
