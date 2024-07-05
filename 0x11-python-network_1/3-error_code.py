#!/usr/bin/python3
''' using urllib to send a request'''

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # get a request to the url
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except error.HTTPError as e:
        # handle http errors and print the status codes
        print("Error code: {}".format(e.code))
