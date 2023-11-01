#!/usr/bin/python3
"""
Rectangle class."""


class Rectangle:
    """Representing.."""

    def __init__(self, width=0, height=0):
        """Initializeing"""
        self.width = width
        self.height = height

    @property
    def _width(self):
        """set the width"""
        return self.__width

    @width.setter
    def _width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def _height(self):
        """set the height"""
        return self.__height

    @height.setter
    def _height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def _area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def _per(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
