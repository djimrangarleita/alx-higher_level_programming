#!/usr/bin/python3
"""Print response or custom message"""

import requests
import sys


def print_response():
    payload = {}
    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        r = r.json()
        if not r:
            print('No result')
            return
        print('[{}] {}'.format(r.get('id'), r.get('name')))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    print_response()
