#!/usr/bin/python3
""" script that takes in letter & sends
    POST request to http://0.0.0.0:5000/search_user with
    letter as parameter.
"""

import requests
import sys

if __name__ == "__main__":
    req_val = ""
    if len(sys.argv) > 1:
        req_val = sys.argv[2]
    req_res = requests.post("http://0.0.0.0:5000/search_user",
                            data={"q": req_val})
    try:
        req_res = req_res.json()
        if len(req_res):
            print("[{}] {}".format(req_res.get("id"), req_res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
