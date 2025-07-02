#!/usr/bin/python3
from urllib import request, error
import sys
try:
    with request.urlopen(sys.argv[1]) as response:
        body = response.read().decode('utf-8')
        print(body)
except error.HTTPError as e:
    print(f"Error code: {e.code}")

