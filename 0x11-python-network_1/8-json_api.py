#!/usr/bin/python3
""" script that takes in letter & sends
    POST request to http://0.0.0.0:5000/search_user with
    letter as parameter.
"""

from sys import argv
import requests


if __name__ == "__main__":
    req_lett = "" if len(argv) == 1 else argv[1]
    pst_req = requests.post("http://0.0.0.0:5000/search_user", {"q": req_lett})

    try:
        post_resp = pst_req.json()
        if post_resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(post_resp.get("id"), post_resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
