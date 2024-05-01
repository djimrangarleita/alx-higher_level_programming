#!/usr/bin/python3
"""Request github public info and print id"""

import requests
import sys


def request_info():
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                                                          sys.argv[2]))
    r = r.json()
    print(r.get('id'))


if __name__ == '__main__':
    request_info()
