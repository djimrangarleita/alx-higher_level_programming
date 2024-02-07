#!/usr/bin/python3
"""Module used to write to a file"""


def append_write(filename="", text=""):
    """Append text to a file"""
    nchars = 0
    with open(filename, 'a', encoding='utf-8') as f:
        nchars = f.write(text)
    return nchars
