#!/bin/bash
# sends request to a URL, & displays only status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
