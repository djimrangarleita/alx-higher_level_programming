#!/usr/bin/python3


"""Module that conatins a function that checks if obj is instance of class"""


def is_same_class(obj, a_class):
    """Check if obj instance of class a_class"""
    return type(obj) is a_class
