#!/usr/bin/python3
"""Define json"""
import json


def load_from_json_file(filename):
    """Createing"""
    with open(filename) as f:
        return json.load(f)
