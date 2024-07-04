#!/bin/bash
# sends a json post and request to given url with given json file.
curl -s -H "content-Type: application/json" -d "$(cat "$2")" "$1"
