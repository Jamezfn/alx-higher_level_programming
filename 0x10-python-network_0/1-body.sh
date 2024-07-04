#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response if the status code is 200
curl -s -o -w "%{http_code}" "$1" | { read body status; [ "$status" = "200" ] && echo "$body"; }
