#!/usr/bin/python3
"""Module used to convert to object from json"""
import json


def from_json_string(my_str):
    """Return an object"""
    return json.loads(my_str)
