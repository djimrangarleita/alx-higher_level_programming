#!/usr/bin/python3


"""This module contains a class named Square"""


class Square:
    """Square class that does nothing that has an instance attr"""

    def __init__(self, size=0):
        """Initialize a private instance attr, size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
