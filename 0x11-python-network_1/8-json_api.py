#!/usr/bin/python3
"""Print response or custom message"""

import requests
import sys


def print_response():
    q_str = ''
    if len(sys.argv) > 1:
        q_str = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q_str})
    try:
        r = r.json()
        if not r:
            print('No result')
            return
        print('[{}] {}'.format(r.get('id'), r.get('name')))
    except json.decoder.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    print_response()
