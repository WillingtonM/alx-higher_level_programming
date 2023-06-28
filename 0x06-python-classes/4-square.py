#!/usr/bin/python3
"""Define class Square."""

class Square:
    """Represent square object."""

    def __init__(self, size=0):
        """Initialize new square object.

        Args:
            size (int): The size of new square object.
        """
        self.size = size

    @property
    def size(self):
        """Get or set current size of the square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of Square object."""
        return (self.__size * self.__size)
