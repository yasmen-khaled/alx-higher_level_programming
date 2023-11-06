#!/usr/bin/python3
"""Defines function"""


def add_attribute(obj, att, value):
    """Add a new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
