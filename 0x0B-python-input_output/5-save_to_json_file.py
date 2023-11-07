#!/usr/bin/python3
"""Define file-writing jason"""
import json


def save_to_json_file(my_obj, filename):
    """Write object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
