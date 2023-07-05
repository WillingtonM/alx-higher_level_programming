#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Defines implementation of rectangle

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width: Width of the new rectangle.
            height: Height of the new rectangle.
        """
        self.height = height
        self.width = width

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
        """Get or set height of Rectangle."""
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
        """Returns rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect_list = []
        for x in range(self.__height):
            [rect_list.append(str(self.print_symbol)) for j in range(self.__width)]
            if x != self.__height - 1:
                rect_list.append("\n")
        return ("".join(rect_list))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        rect_list = "Rectangle(" + str(self.__width)
        rect_list += ", " + str(self.__height) + ")"
        return (rect_list)

    def __del__(self):
        """Print a message for every deletion of
        the rectangle.

        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with greater area.

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Fecond rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with
        width == height == size

        Args:
            size (int): The width and height of the new Rectangle.

        """
        return (cls(size, size))
