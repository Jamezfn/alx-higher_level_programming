#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import requests
response = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type: ', type(response.text))
print('\t- content: ', response.text)
