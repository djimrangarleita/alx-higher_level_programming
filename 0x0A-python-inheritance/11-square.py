#!/usr/bin/python3
"""Module Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        if self.integer_validator('size', size) is None:
            self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String representation of the object"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
