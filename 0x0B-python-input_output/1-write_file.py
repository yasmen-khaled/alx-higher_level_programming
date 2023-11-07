#!/usr/bin/python3
"""Define a file-writing """


def write_file(filename="", text=""):
    """Write a string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
