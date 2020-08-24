#!/usr/bin/python3
"""POST an email
"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]

    values = {}
    values['email'] = mail
    data = parse.urlencode(values)
    data = data.encode()
    req = request.Request(url, data=data)  # Key for POST
    with request.urlopen(req) as response:
        print(response.read().decode())
