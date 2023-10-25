#!/usr/bin/python3
"""class"""


class Square:
    """Representing"""

    def __init__(self, size=0):
        """new square"""
        if not isinstance(size, int):
            raise TypeError("")
        elif size < 0:
            raise ValueError("")
        self.__size = size

    def area(self):
        """Returning current area."""
        return (self.__size * self.__size)
