#!/usr/bin/python3
"""script that takes in URL, sends request to URL displays
    value of X-Request-Id variable found in header of response.
"""

from urllib import request
import sys

if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as req_res:
        print(dict(req_res.headers).get('X-Request-Id'))
