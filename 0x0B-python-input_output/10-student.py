#!/usr/bin/python3
"""Module to return dict description of an object"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Object initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This func returns a dict description of an object"""
        if attrs is not None:
            return {key: getattr(self, key) for key in attrs
                    if key in list(self.__dict__)}
        return self.__dict__
