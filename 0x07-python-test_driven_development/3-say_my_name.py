#!/usr/bin/python3
"""Module with a function that will say your name"""


def say_my_name(first_name, last_name=""):
    """Takes two positional string args and say your"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
