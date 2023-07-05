#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        numb_of_instances (int): The number of Rectangle instances.
    """

    numb_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width: Width of the new rectangle.
            height: Height of the new rectangle.
        """
        type(self).numb_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of Rectangle."""
        return ( self.__height * self.__width)

    def perimeter(self):
        """Return perimeter of Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ( (self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return printable representation of Rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect_list = []
        for x in range(self.__height):
            [rect_list.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect_list.append("\n")
        return ("".join(rect_list))

    def __repr__(self):
        """Return string representation of Rectangle."""
        rect_list = "Rectangle(" + str(self.__width)
        rect_list += ", " + str(self.__height) + ")"
        return (rect_list)

    def __del__(self):
        """Print message for deletion of Rectangle."""
        type(self).numb_of_instances -= 1
        print("Bye rectangle...")
