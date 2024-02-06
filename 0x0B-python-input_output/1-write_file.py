#!/usr/bin/python3
"""Module used to write to a file"""


def write_file(filename="", text=""):
    """Write to a file"""
    nchars = 0
    with open(filename, 'w', encoding='utf-8') as f:
        nchars = f.write(text)
    return nchars
