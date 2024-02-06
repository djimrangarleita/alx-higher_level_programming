#!/usr/bin/python3
"""Module with one function"""


def read_file(filename=""):
    """Function that reads a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
