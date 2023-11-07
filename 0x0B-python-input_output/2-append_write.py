#!/usr/bin/python3
"""Define file-appending"""


def append_write(filename="", text=""):
    """Appends str"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
