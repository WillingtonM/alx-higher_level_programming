#!/usr/bin/python3
""" script that takes in URL and email address, sends
    POST request to passed URL with email as parameter,
    & finally displays body of response.

    Usage: ./6-post_email.py <URL> <email>
        Displays body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    dta = {'email': sys.argv[2]}
    req_res = requests.post(sys.argv[1], dta=dta)
    print(req_res.text)
