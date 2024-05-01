#!/usr/bin/python3
"""Print response or custom message"""

import requests
import sys


def print_response():
    q_str = ''
    if len(sys.argv) > 1:
        q_str = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data={'q': q_str})
    # print(q_str)
    # r = requests.post('https://www.mossosouk.com',
    #                  params={'q': q_str})
    # print(r.url)
    try:
        r = r.json()
        if not r:
            print('No result')
            return
        print(f'[{r.id}] {r.name}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')


if __name__ == '__main__':
    print_response()
