#!/usr/bin/python3
"""Define CLASS"""


class MyInt(int):
    """Inverting int"""

    def __eq__(self, value):
        """override == opeartor"""
        return self.real != value

    def __ne__(self, value):
        """override != operator"""
        return self.real == value
