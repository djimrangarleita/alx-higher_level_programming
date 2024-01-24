#!/usr/bin/python3


"""This module contains a class named Square"""


class Square:
    """Square class that has an instance attr and some instance methods"""

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
        return self.__size ** 2

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
