#!/usr/bin/python3
"""class Square."""


class Square:
    """Representing"""

    def __init__(self, size):
        """new_square"""
        self.size = size

    @property
    def size(self):
        """set the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area"""
        return (self.__size * self.__size)
