#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rtable = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

    ntable = list(map(lambda x: rtable[x], roman_string))
    filtered = []
    i = 0
    while (i < len(ntable)):
        if i < len(ntable) - 1 and ntable[i] < ntable[i + 1]:
            filtered.append(ntable[i + 1] - ntable[i])
            i += 1
        else:
            filtered.append(ntable[i])
        i += 1
    return reduce(lambda x, y: x + y, filtered)
