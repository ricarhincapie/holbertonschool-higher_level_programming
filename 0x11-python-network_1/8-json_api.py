#!/usr/bin/python3
"""Fetches an URL and displays response body
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://de0f2fdee31c.ff38d7df.hbtn-cod.io:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        response.raise_for_status()
        json_response = response.json()
        if (len(json_response)) == 0:
            print("No result")
        if (len(json_response)) > 0:
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except Exception as err:
        print("Not a valid JSON")
