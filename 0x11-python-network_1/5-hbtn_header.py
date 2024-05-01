#!/usr/bin/python3
"""Print request header, key X-Request-Id"""

import requests
import sys


def print_header():
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == '__main__':
    print_header()
