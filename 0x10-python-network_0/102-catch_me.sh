#!/bin/bash
# Send a POST request to 0.0.0.0:5000/catch_me to get "You got me!" response
curl -s -X POST -H "User-Id: 98" http://127.0.0.1:5000/catch_me
