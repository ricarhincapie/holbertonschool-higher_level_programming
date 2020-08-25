#!/usr/bin/python3
"""Fetches an URL and displays response body
"""
if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    cont_type = (type(response.text))
    cont_ = response.text
    print("Body response:")
    print("\t- type:", cont_type)
    print("\t- content:", cont_)
