#!/usr/bin/python3
""" Find a peak in a list of integers """


def find_peak(ints):
    """ Find peak in a list of integers """
    if not ints:
        return None
    if len(ints) <= 2:
        return max(ints)
    if ints[0] >= ints[1]:
        return ints[0]
    i = 1
    while (i < len(ints) - 1):
        if ints[i] >= ints[i - 1] and ints[i] >= ints[i + 1]:
            return ints[i]
        i += 1
    return ints[-1]
