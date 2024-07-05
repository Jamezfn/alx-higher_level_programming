#!/usr/bin/python3
'''Using the github api to display my id'''

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)

    #send a get request to the github api
    response = requests.get(url, auth=auth)
    print(response.json()get("id"))
