#!/usr/bin/python3
"""Fetches an URL and displays header X-Request-Id
"""
if __name__ == "__main__":
    from urllib import request
    import sys

    arg = sys.argv[1]
    with request.urlopen(arg) as response:
        html = response.info()
        print(html['X-Request-Id'])
