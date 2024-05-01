#!/usr/bin/python3
"""Send post request and print response"""

import urllib.request
import sys


def send_email():
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))


if __name__ == '__main__':
    send_email()
