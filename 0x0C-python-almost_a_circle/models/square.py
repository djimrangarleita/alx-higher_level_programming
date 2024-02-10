#!/usr/bin/python3
"""Module that contains the class Square"""
from . import rectangle


class Square(rectangle.Rectangle):
    """Class Square that inherit from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y,
                self.width)
