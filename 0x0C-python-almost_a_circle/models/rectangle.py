#!/usr/bin/python3
"""
Module that contains the class Rectangle
"""
from . import base


class Rectangle(base.Base):
    """Class rectangle that contains the definition of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization with parents init and local instance attrs

        Args:
            id (int, optional): id of the class
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): instance attr
            y (int, optional): instance attr
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """Getter for the property x of the triangle"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Getter for the property y"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
