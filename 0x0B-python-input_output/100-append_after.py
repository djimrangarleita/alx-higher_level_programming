#!/usr/bin/python3
"""Module comment"""


def append_after(filename="", search_string="", new_string=""):
    """Please implement me"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = ""
        for line in f:
            data += line
            if search_string in line:
                data += new_string

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
