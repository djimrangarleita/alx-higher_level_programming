#!/usr/bin/python3


"""Module with a class that inherit the list class"""


class MyList(list):
    """A class that inherit from list and define 1 method"""
    def __init__(self):
        """Initialize a list object"""
        list.__init__(self)

    def print_sorted(self):
        """Print list sorted in asc"""
        print(sorted(self))
