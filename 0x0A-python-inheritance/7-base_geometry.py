#!/usr/bin/python3
"""Defines class """


class BaseGeometry:
    """Reprsent base"""

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter"""
  
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
