#!/usr/bin/python3
"""Defines  Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing"""

    def __init__(self, size):
        """Initializeing"""
      
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
