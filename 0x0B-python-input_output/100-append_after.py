#!/usr/bin/python3
"""Module comment"""


def append_after(filename="", search_string="", new_string=""):
    """Please implement me"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line_number = 1
    for line in lines:
        if search_string in line:
            lines.insert(line_number, new_string)
        line_number += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
