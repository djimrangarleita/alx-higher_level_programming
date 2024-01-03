#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    sign = 1
    if b < 0:
        sign = -1
        b *= -1
    res = a
    for i in range(1, b):
        res *= a
    if sign < 0:
        res = 1 / res

    return res
