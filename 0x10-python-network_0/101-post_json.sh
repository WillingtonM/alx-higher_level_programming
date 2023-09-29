#!/bin/bash
# sends JSON POST request to URL, & displays body of response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
