#!/usr/bin/python3
"""class Square."""


class Square:
    """Representing"""

    def __init__(self, size=0, position=(0, 0)):
        """new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size"""
        return (self.__size)

    @size.setter
    def size(self, valu):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif valu < 0:
            raise ValueError("size must be >= 0")
        self.__size = valu

    @property
    def position(self):
        """set the current position"""
        return (self.__position)

    @position.setter
    def position(self, valu):
        if (not isinstance(valu, tuple) or
                len(valu) != 2 or
                not all(isinstance(num, int) for num in valu) or
                not all(num >= 0 for num in valu)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = valu

    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for xo in range(0, self.__size):
            [print(" ", end="") for ox in range(0, self.__position[0])]
            [print("#", end="") for oxox in range(0, self.__size)]
            print("")
