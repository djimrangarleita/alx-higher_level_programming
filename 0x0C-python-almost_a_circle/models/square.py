#!/usr/bin/python3
"""Module that contains the class Square"""
from . import rectangle


class Square(rectangle.Rectangle):
    """Class Square that inherit from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y,
                self.width)

    @property
    def size(self):
        """Getter the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update attrs of a Square"""
        args = list(args)
        if len(args) >= 2:
            args.insert(2, args[1])
        if kwargs.get('size'):
           size = kwargs.pop('size')
           kwargs['width'] = size
           kwargs['height'] = size
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """Return the dict rep of a square"""
        square_dict = super().to_dictionary()
        square_dict['size'] = square_dict.pop('width')
        del square_dict['height']
        return square_dict
