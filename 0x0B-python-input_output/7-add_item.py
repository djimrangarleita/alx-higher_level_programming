#!/usr/bin/python3
"""Module used to convert from/to json"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename="add_item.json"):
    """Create json file"""
    objdata = []
    try:
        objdata = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    objdata += sys.argv[1:]
    save_to_json_file(objdata, filename)


add_item()
