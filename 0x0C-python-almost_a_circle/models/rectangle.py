#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class."""
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        super().__init__(id)

    @property
    def x(self):
        """Get or set the x coordinate."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the x coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self._x = value

    @property
    def y(self):
        """Get or set the y coordinate."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the y coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self._y = value

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Display the Rectangle."""
        for _ in range(self.y):
            print('\n', end="")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
