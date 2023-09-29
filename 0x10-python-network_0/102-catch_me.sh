#!/bin/bash
# Script that makes request to 0.0.0.0:5000/catch_me & get response
curl -sX PUT -L -d "user_id=98" -H "Origin: You got me!" "0.0.0.0:5000/catch_me"
