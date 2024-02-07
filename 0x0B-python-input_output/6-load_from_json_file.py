#!/usr/bin/python3
import json


"""Module used to convert from/to json"""


def load_from_json_file(filename):
    """Create json file from an object"""
    json_data = ''
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = f.read()

    return json.loads(json_data)
