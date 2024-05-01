#!/usr/bin/python3
"""Print request body or status code in case of error"""

import requests
import sys


def print_request():
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print('Error code:', r.status_code)


if __name__ == '__main__':
    print_request()
