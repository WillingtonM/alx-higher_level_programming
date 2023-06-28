#!/usr/bin/python3
"""Define class Square."""

class Square:
    """Represent square."""

    def __init__(self, size):
        """Initialize new square object object.

        Args:
            size (int): The size of new square object.
        """
        self.size = size

    @property
    def size(self):
        """Get or set current size of square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square object with # character."""
        for x in range(0, self.__size):
            for y in range(self.__size):
                print("#", end='')
            print("")
        if self.__size == 0:
            print("")
