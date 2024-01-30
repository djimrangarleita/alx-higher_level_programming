#!/usr/bin/python3
"""Module with one function to add ints"""


def add_integer(a, b=98):
    """Add two integers/floats and return the result"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
