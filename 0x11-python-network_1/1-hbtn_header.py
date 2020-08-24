#!/usr/bin/python3
"""Fetches an URL and displays header X-Request-Id
"""
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.info()
        print(html['X-Request-Id'])
