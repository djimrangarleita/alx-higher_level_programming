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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for the property x of the triangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for the property y"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Calculate and return the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Display a rectangle according to its sizes"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(' ' * self.x, end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """Return the string representation of the current occurence"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

    def update(self, *args, **kwargs):
        """Update the current rectangle with new attr values"""
        keys = ['id', 'width', 'height', 'x', 'y']
        if args:
            if len(args) > len(keys):
                raise ValueError('too many values to unpack')
            for i, arg in enumerate(args):
                setattr(self, keys[i], arg)
        else:
            for key, arg in kwargs.items():
                if key in keys:
                    setattr(self, key, arg)

    def to_dictionary(self):
        """Return the dict representation of a rectangle"""
        keys = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in keys}
