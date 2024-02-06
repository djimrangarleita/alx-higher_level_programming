#!/usr/bin/python3


"""Module that conatins a function that checks if obj inherits from class"""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
