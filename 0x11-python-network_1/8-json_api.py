#!/usr/bin/python3
"""Print response or custom message"""

import requests
import json
import sys


def print_response():
    payload = {}
    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        r = r.json()
        if r:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
        else:
            print('No result')
    except json.decoder.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    print_response()
