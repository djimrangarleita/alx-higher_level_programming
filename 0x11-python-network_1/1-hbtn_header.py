#!/usr/bin/python3
"""Print request header, key X-Request-Id"""

import urllib.request
import sys


def print_header():
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    print_header()
