#!/usr/bin/python3
import json


"""Module used to convert to object from json"""


def from_json_string(my_str):
    """Return an object"""
    return json.loads(my_str)
