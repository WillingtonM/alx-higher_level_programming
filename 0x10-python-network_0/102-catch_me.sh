#!/bin/bash
# Script that makes request to 0.0.0.0:5000/catch_me & get response
curl -X POST -d "user_id=42" 0.0.0.0:5000/catch_me
