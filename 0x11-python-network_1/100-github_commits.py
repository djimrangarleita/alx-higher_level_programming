#!/usr/bin/python3
"""List commit history"""

import requests
import sys


def request_commit():
    r_url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                                sys.argv[1])
    r = requests.get(r_url)
    r = r.json()
    i = 0
    while i < 10:
        print('{}: {}'.format(r[i].get('sha'),
              r[i]['commit']['author']['name']))
        i += 1


if __name__ == '__main__':
    request_commit()
