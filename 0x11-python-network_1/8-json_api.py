#!/usr/bin/python3
""" a Python script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    val = ""
    if len(sys.argv) > 1:
        val = sys.argv[2]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": val})
    try:
        r = r.json()
        if len(r):
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
