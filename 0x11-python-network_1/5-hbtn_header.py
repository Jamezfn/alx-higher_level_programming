#!/usr/bin/python3
import requests
import sys
response = requests.get(sys.argv[1])
print(response.headers.get('X-Request-Id'))
