#!/usr/bin/python3
"""Module with fn that adds new attr to an object"""


def add_attribute(obj, name, attr):
    """Function that adds new attr to an object"""
    if (obj.__class__.__module__ == 'builtins'):
        raise TypeError('can\'t add new attribute')
    obj.name = attr
