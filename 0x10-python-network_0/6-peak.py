#!/usr/bin/python3
""" Find a peak in a list of integers """


def find_peak(list_of_integers):
    """ Find peak in a list of integers """
    if not list_of_integers:
        return None
    return max(list_of_integers)
