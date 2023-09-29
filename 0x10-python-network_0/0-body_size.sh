#!/bin/bash
# send request to URL with curl, & displays size of body of response
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
