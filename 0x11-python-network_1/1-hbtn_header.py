#!/usr/bin/python3
"""Change me"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
