#!/usr/bin/python3
"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height is less than or equal to 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y is less than 0.
        """
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        super().__init__(id)

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self._width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self._height = value

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than or equal to 0")
        self._x = value

    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greater than or equal to 0")
        self._y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self._width * self._height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self._width == 0 or self._height == 0:
            print("")
            return

        [print("") for _ in range(self._y)]
        for _ in range(self._height):
            [print(" ", end="") for _ in range(self._x)]
            [print("#", end="") for _ in range(self._width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (int): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represents height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    if arg is None:
                        self.__init__(self._width, self._height, self._x, self._y)
                    else:
                        self._id = arg
                elif i == 1:
                    self._width = arg
                elif i == 2:
                    self._height = arg
                elif i == 3:
                    self._x = arg
                elif i == 4:
                    self._y = arg

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self._width, self._height, self._x, self._y)
                    else:
                        self._id = value
                elif key == "width":
                    self._width = value
                elif key == "height":
                    self._height = value
                elif key == "x":
                     self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
