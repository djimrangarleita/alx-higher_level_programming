#!/usr/bin/python3
"""Module used to convert object to json and store in file"""
import json


def save_to_json_file(my_obj, filename):
    """Create json file from an object"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
