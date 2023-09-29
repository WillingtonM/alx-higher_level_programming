#!/usr/bin/python3
"""get thy properties from mail"""

if __name__ == '__main__':
    import sys
    import requests

    req_headers = {}
    req_headers['Authorization'] = '{} {}'.format(sys.argv[0], sys.argv[1])
    req_res = requests.get('https://api.github.com/users/{}'
                           .format(sys.argv[1]), req_headers=req_headers)
    print(req_res.json().get('id'))
