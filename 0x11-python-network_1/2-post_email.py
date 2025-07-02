#!/usr/bin/python3
"""
Takes in a URL and an Email, sends a POST request to the
passed URL with the email as a parameter and displays the body
the response
"""
from urllib import request, parse
import sys

data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
with request.urlopen(sys.argv[1], data) as response:
    body = response.read().decode('utf-8')
    print(body)
