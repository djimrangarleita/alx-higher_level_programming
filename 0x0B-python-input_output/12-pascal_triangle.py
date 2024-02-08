#!/usr/bin/python3
"""Module comment"""


def pascal_triangle(n):
    """Pascal triangle function"""
    if n <= 0:
        return []

    result = [[1]]
    for i in range(n):
        lastrow = result[-1]
        tmp = [0] + lastrow + [0]
        currow = []
        for j in range(len(lastrow) + 1):
            currow.append(tmp[j] + tmp[j + 1])
        result.append(currow)

    return result
