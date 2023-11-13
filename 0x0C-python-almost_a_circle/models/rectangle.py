#!/usr/bin/python3

from models.base import Base


"""Defines a rectangle class."""


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x_pos=0, y_pos=0, identifier=None):
        """Initialize a new instance of the Rectangle class"""
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__width = width
        self.__height = height
        super().__init__(identifier)

    @property
    def x_pos(self):
        """Returns the x position"""
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, value):
        """Set the x position"""
        if type(value) is not int:
            raise TypeError("x_pos must be an integer")
        self.__x_pos = value

    @property
    def y_pos(self):
        """Returns the y position"""
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, value):
        """Set the y position"""
        if type(value) is not int:
            raise TypeError("y_pos must be an integer")
        self.__y_pos = value

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the object"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the object"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Display the Rectangle"""
        for _ in range(self.y_pos):
            print('\n', end="")
        for _ in range(self.height):
            for _ in range(self.x_pos):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.identifier,
            self.x_pos,
            self.y_pos,
            self.width,
            self.height
            )

    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x_pos, self.y_pos)
                    else:
                        self.identifier = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x_pos = arg
                elif a == 4:
                    self.y_pos = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "identifier":
                    if v is None:
                        self.__init__(self.width, self.height, self.x_pos, self.y_pos)
                    else:
                        self.identifier = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x_pos":
                    self.x_pos = v
                elif k == "y_pos":
                    self.y_pos = v

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle"""
        return {
            "identifier": self.identifier,
            "width": self.width,
            "height": self.height,
            "x_pos": self.x_pos,
            "y_pos": self.y_pos
            }
