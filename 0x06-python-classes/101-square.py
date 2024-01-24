#!/usr/bin/python3


"""This module contains a class named Square"""


class Square:
    """Square class that has an instance attr and some instance methods"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a private instance attr, size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of a square"""
        return self.size ** 2

    def my_print(self):
        """Print a square"""
        if self.size == 0:
            return ""
        for h in range(self.position[1]):
            print()
        for i in range(self.size):
            if self.position[0]:
                print(" " * self.position[0], end="")
            for j in range(self.size):
                print("#", end="")
            print("")


    def __repr__(self):
        self.my_print()
        return ""
