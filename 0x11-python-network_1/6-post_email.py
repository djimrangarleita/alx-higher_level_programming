#!/usr/bin/python3
"""Send post request and print response"""

import requests
import sys


def send_email():
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)


if __name__ == '__main__':
    send_email()
