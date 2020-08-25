#!/usr/bin/python3
"""Fetches commits from users
"""
if __name__ == "__main__":

    import requests
    import sys

    rep_name = sys.argv[1]
    own_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        own_name, rep_name)
    response = requests.get(url)
    json_response = response.json()
    i = 0
    while i < 10:
        sha = json_response[i].get('sha')
        auth = json_response[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, auth))
        i = i + 1
