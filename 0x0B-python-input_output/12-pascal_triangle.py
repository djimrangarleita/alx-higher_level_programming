#!/usr/bin/python3
"""Module comment"""


def pascal_triangle(n):
    """Pascal triangle function"""
    result = []
    for i in range(n):
        result.append([int(x) for x in str(11**i)])
    return result
