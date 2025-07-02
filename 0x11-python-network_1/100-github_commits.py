#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{repo}/{owner}/commits?per_page'
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print("None")
