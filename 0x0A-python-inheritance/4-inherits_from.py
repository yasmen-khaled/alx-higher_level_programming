#!/usr/bin/python3
"""Define class"""


def inherits_from(obj, a_class):
    """Checks object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
