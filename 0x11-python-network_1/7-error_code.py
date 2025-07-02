#!/usr/bin/python3
import requests
import sys

response = requests.get(sys.argv[1])
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
