#!/usr/bin/python3
''' using request module to send a request to the url'''

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = request.get(url)
    print(response.headers.get('X-Request-Id'))
