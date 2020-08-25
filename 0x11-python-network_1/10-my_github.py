#!/usr/bin/python3
"""Fetches My Githib id
"""
if __name__ == "__main__":

    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    json_response = response.json()
    if json_response.get('message') == 'Bad credentials':
        print(None)
    else:
        print(json_response.get('id'))
