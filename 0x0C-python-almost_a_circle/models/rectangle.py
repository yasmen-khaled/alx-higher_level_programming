#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class derived from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle object."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters."""
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a formatted string representation of the object."""
        id = self.id
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """Update the attributes of the object."""
        if args is not None and len(args) != 0:
            a = len(args)
            if a >= 1:
                self.id = args[0]
            if a >= 2:
                self.__width = args[1]
            if a >= 3:
                self.__height = args[2]
            if a >= 4:
                self.__x = args[3]
            if a >= 5:
                self.__y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Return the object as a dictionary."""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x,
                "y": self.__y}
