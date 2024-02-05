#!/usr/bin/python3
"""Module Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        if self.integer_validator('width', width) is None:
            self.__width = width
        if self.integer_validator('height', height) is None:
            self.__height = height

    def area(self):
        """Compute and return the area of the current rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the object"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
