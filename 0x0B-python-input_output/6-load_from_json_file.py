#!/usr/bin/python3
"""Define json"""
import json


def save_to_json_file(my_obj, filename):
    """Write object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
