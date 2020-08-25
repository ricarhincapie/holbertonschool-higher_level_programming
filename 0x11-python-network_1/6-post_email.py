#!/usr/bin/python3
"""Fetches an URL and displays response body
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
