#!/usr/bin/python3
"""Takes is a URL and displays body or error code
"""
if __name__ == "__main__":
    from urllib import request, error
    import sys

    arg = sys.argv[1]
    try:
            with request.urlopen(arg) as response:
                html = response.read()
                print(html.decode())
    except error.HTTPError as err:
            print("Error code:", err.code)
