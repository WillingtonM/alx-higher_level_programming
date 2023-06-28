#!/usr/bin/python3
"""Define Square class."""

class Square:
    """Define class Square"""

    def __init__(self, size=0):
        """Initialize new square object.

        Args:
           size (int): The size of new square object.
        """
        self.size = size

    @property
    def size(self):
        """ Get size of Square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Return area of Square object."""
    def area(self):
        return (self.__size * self.__size)

    """Defines == comparision."""
    def __eq__(self, other):
        return self.area() == other.area()

    """ Define != comparision."""
    def __ne__(self, other):
        return self.area() != other.area()

    """ Define < comparision."""
    def __lt__(self, other):
        return self.area() < other.area()
    """True if self is greater than other"""
    def __gt__(self, other):
        return self.area() > other.area()
    """Define <= comparision."""
    def __le__(self, other):
        return self.area() <= other.area()

    """ Define >= comparision."""
    def __ge__(self, other):
        return self.area() >= other.area()
