#!/usr/bin/python3


"""This module contains the class Rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instance initializer"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return the width of the current(instance) rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the current rectangle"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Return the height of the current(instance) rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the current rectangle"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
