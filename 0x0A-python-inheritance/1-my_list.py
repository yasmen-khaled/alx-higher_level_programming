#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """sorted printing"""

    def print_sorted(self):
        """Print list"""
        print(sorted(self))
