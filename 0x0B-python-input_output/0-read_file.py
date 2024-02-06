#!/usr/bin/python3
"""Module with one function"""


def read_file(filename=""):
    """Function that reads a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content.rstrip())
