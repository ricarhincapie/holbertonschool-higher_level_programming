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

    for count, comm in enumerate(json_response):
        if count < 10:
            sha = comm.get('sha')
            auth = comm.get('commit').get('author').get('name')
            print("{}: {}".format(sha, auth))
        else:
            exit()
