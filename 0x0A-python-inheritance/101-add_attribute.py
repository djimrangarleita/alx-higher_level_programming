#!/usr/bin/python3
"""Module with fn that adds new attr to an object"""


def add_attribute(obj, name, attr):
    """Function that adds new attr to an object"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, attr)
