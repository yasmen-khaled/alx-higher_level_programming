#!/usr/bin/python3
# square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square object."""
        if args and len(args) != 0:
            arg_index = 0
            for arg in args:
                if arg_index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_index == 1:
                    self.size = arg
                elif arg_index == 2:
                    self.x = arg
                elif arg_index == 3:
                    self.y = arg
                arg_index += 1
        elif kwargs and len(kwargs) != 0:
            if 'id' in kwargs:
                if kwargs["id"] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
