#!/usr/bin/python3
"""Module that prints a square"""


def print_square(size):
    """Takes the size of the string to print"""
    if type(size) not in [int, float]:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    square = ''
    for i in range(int(size)):
        for j in range(int(size)):
            square += '#'
        if i < int(size) - 1:
            square += '\n'
    print(square)
