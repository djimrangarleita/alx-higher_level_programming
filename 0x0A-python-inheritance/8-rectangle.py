#!/usr/bin/python3
"""Module Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        if self.integer_validator('width', width) is None:
            self.__width = width
        if self.integer_validator('height', height) is None:
            self.__height = height
