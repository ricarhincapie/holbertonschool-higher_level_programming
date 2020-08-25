#!/usr/bin/python3
"""Fetches an URL and displays response body
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code:", response.status_code)
