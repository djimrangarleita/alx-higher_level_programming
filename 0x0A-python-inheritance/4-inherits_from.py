#!/usr/bin/python3


"""Module that conatins a function that checks if obj inherits from class"""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class"""
    return issubclass(type(obj), a_class)
