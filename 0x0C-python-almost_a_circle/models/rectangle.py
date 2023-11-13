#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

class Rect(Base):
    """Represent a rectangle."""

    def __init__(self, rect_width, rect_height, rect_x=0, rect_y=0, rect_id=None):
        """Initialize a new Rectangle."""
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect_x = rect_x
        self.rect_y = rect_y
        super().__init__(rect_id)

    @property
    def rect_width(self):
        """Set/get the width of the Rectangle."""
        return self.__rect_width

    @rect_width.setter
    def rect_width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__rect_width = value

    @property
    def rect_height(self):
        """Set/get the height of the Rectangle."""
        return self.__rect_height

    @rect_height.setter
    def rect_height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__rect_height = value

    @property
    def rect_x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__rect_x

    @rect_x.setter
    def rect_x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__rect_x = value

    @property
    def rect_y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__rect_y

    @rect_y.setter
    def rect_y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__rect_y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.rect_width * self.rect_height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.rect_width == 0 or self.rect_height == 0:
            print("")
            return

        [print("") for y in range(self.rect_y)]
        for h in range(self.rect_height):
            [print(" ", end="") for x in range(self.rect_x)]
            [print("#", end="") for w in range(self.rect_width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.rect_width, self.rect_height, self.rect_x, self.rect_y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.rect_width = arg
                elif a == 2:
                    self.rect_height = arg
                elif a == 3:
                    self.rect_x = arg
                elif a == 4:
                    self.rect_y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.rect_width, self.rect_height, self.rect_x, self.rect_y)
                    else:
                        self.id = v
                elif k == "width":
                    self.rect_width = v
                elif k == "height":
                    self.rect_height = v
                elif k == "x":
                    self.rect_x = v
                elif k == "y":
                    self.rect_y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.rect_width,
            "height": self.rect_height,
            "x": self.rect_x,
            "y": self.rect_y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.rect_x, self.rect_y,
                                                       self.rect_width, self.rect_height)
