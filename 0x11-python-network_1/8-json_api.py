#!/usr/bin/python3
import requests
import sys
q = sys.argv[1] if len(sys.argv) > 1 else ""
response = requests.post('http://192.168.1.101:5000/search_user', data ={'q': q})
try:
    json_data = response.json()
    if json_data and 'id' in json_data and 'name' in json_data:
        print(f"[{json_data['id']}] {json_data['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
