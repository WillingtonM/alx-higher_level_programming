#!/usr/bin/python3
"""send post requestwith mail"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    req_ls = sys.argv
    vals = {}
    vals['email'] = req_ls[2]
    dta = urllib.parse.urlencode(vals)
    dta = dta.encode('ascii')
    req = urllib.request.Request(req_ls[1], dta)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
