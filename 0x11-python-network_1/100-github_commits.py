#!/usr/bin/python3
""" Lists 10 commits from most recent to oldest of
    repository "rails" by user "rails"
    Usage: ./100-github_commits.py <repo name> <owner>
"""
from sys import argv
import requests

if __name__ == "__main__":
    req_repo = argv[1]
    rep_owner = argv[2]
    req_url = "https://api.github.com/repos/{}/{}/commits".format(
        rep_owner, req_repo)

    req_res = requests.get(req_url)
    commits = req_res.json()
    try:
        for num in range(10):
            print("{}: {}".format(commits[num].get("sha"),
                  commits[num].get("commit").get("author").get("name")))
    except IndexError:
        pass
