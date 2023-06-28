#!/usr/bin/python3
"""Define class Square."""

class Square:
    """Represent square object."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square object.

        Args:
            size (int): Size of new square object.
            position (int, int): Position of new square object.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the current position of square object."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current area of square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square object with the # character."""
        if self.__size == 0:
            print("")
            return
        
        [print("") for j in range(0, self.__position[1])]

        for x in range(0, self.size):
            for k in range(self.position[0]):
                print(" ", end='')
            for j in range(self.size):
                print("#", end='')
            print()
