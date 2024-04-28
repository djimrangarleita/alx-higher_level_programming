#!/usr/bin/python3
"""Change me"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   html = response.read()
   print('Body response:')
   print('\t-type: {}'.format(response.read().decode('utf-8')))
   print('\t-content: {}'.format(response.read()))
   print('\t-utf8 content: {}'.format(response.headers['Content-Type']))
