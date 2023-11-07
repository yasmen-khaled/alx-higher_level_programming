#!/usr/bin/python3
"""Defines text"""


def read_file(filename=""):
    """Printing  contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
