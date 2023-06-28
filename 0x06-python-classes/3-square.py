#!/usr/bin/python3
"""A module for working with squares object"""

class Square:
    """Represent square object."""
    
    def __init__(self, size=0):
        """Initialize a new square object.

        Args:
           size (int): The size of new square object.
        """
        if not isinstance(size, int):
            raise TypeError()
        elif size < 0:
            raise ValueError()
        self.__size = size
    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)
