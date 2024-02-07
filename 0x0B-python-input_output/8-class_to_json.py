#!/usr/bin/python3
"""Module to return dict description of an object"""


def class_to_json(obj):
    """This func returns a dict description of an object"""
    return obj.__dict__
