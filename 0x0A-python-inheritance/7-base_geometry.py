#!/usr/bin/python3
"""Module base geometry that will be inherited by other classes"""


class BaseGeometry:
    """This is base geometry class"""
    def area(self):
        """Raise an exception because method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer for safety"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
