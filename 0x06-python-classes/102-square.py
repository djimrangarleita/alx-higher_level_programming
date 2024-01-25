#!/usr/bin/python3


"""This module contains a class named Square"""


class Square:
    """Square class that does nothing that has an instance attr"""

    def __init__(self, size=0):
        """Initialize a private instance attr, size"""
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of a square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Compute and return the area of a square"""
        return self.size ** 2

    def __eq__(self, other):
        """Compare 2 squares"""
        if not isinstance(other, Square):
            raise NotImplemented
        return self.size == other.size

    def __lt__(self, other):
        """Compare 2 squares, less than"""
        if not isinstance(other, Square):
            raise NotImplemented
        return self.size < other.size

    def __le__(self, other):
        """Compare 2 squares, less than or equal"""
        if not isinstance(other, Square):
            raise NotImplemented
        return self.size <= other.size

    def __gt__(self, other):
        """Compare 2 squares, greater than"""
        if not isinstance(other, Square):
            raise NotImplemented
        return self.size > other.size

    def __ge__(self, other):
        """Compare 2 squares, greater than or equal"""
        if not isinstance(other, Square):
            raise NotImplemented
        return self.size >= other.size
