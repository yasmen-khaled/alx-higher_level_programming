#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        self.properties = {'width': width, 'height': height, 'x': x, 'y': y}
        super().__init__(id)

    def __getitem__(self, key):
        return self.properties[key]

    def __setitem__(self, key, value):
        if type(value) != int:
            raise TypeError(f"{key} must be an integer")
        if value <= 0 and key in ['width', 'height']:
            raise ValueError(f"{key} must be > 0")
        if value < 0 and key in ['x', 'y']:
            raise ValueError(f"{key} must be >= 0")
        self.properties[key] = value

    def area(self):
        """Return the area of the Rectangle."""
        return self['width'] * self['height']

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self['width'] == 0 or self['height'] == 0:
            print("")
            return

        [print("") for y in range(self['y'])]
        for h in range(self['height']):
            [print(" ", end="") for x in range(self['x'])]
            [print("#", end="") for w in range(self['width'])]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        keys = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if arg is None and keys[i] == 'id':
                    self.__init__(self['width'], self['height'], self['x'], self['y'])
                else:
                    self[keys[i]] = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if v is None and k == 'id':
                    self.__init__(self['width'], self['height'], self['x'], self['y'])
                else:
                    self[k] = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self['width'],
            "height": self['height'],
            "x": self['x'],
            "y": self['y']
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self['x'], self['y'],
                                                       self['width'], self['height'])
