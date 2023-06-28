#!/usr/bin/python3
"""Define Square class."""


class Square:
    """Define class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square object.
        Args:
           size (int): Size of new square object.
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
        """Get or set current position of square object."""
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
        """Return area of square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square object with number character."""
        if self.__size == 0:
            print("")
            return
        [print("") for i_ind in range(0, self.__position[1])]

        for i_ind in range(0, self.__size):
            [print(" ", end="") for j_ind in range(0, self.__position[0])]
            [print("#", end="") for k_ind in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define print() representation of a Square object."""
        if self.__size != 0:
            [print("") for i_ind in range(0, self.__position[1])]
        for i_ind in range(0, self.__size):
            [print(" ", end="") for j_ind in range(0, self.__position[0])]
            [print("#", end="") for k_ind in range(0, self.__size)]
            if i_ind != self.__size - 1:
                print("")
        return("")
