#!/usr/bin/python3
"""Print request body or status code in case of error"""

import urllib.request
import sys


def print_request():
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == '__main__':
    print_request()
