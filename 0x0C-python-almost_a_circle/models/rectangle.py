#!/usr/bin/python3
"""Defines rectangle class."""

from models.base import Base

class Rectangle(Base):
    """Represent rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
            x (int): x coordinate of new Rectangle.
            y (int): y coordinate of new Rectangle.
            id (int): Identity of new Rectangle.
        Raises:
            TypeError: If either of height or width is not int.
            ValueError: If either of height or width <= 0.
            TypeError: If either of x or y is not int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set or get width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set or get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set or get x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set or get y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#` character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y_val in range(self.y)]
        for h_val in range(self.height):
            [print(" ", end="") for x_val in range(self.x)]
            [print("#", end="") for w_val in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            ag = 0
            for arg in args:
                if ag == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ag == 1:
                    self.width = arg
                elif ag == 2:
                    self.height = arg
                elif ag == 3:
                    self.x = arg
                elif ag == 4:
                    self.y = arg
                ag += 1

        elif kwargs and len(kwargs) != 0:
            for l, m in kwargs.items():
                if l == "id":
                    if m is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = m
                elif l == "width":
                    self.width = m
                elif l == "height":
                    self.height = m
                elif l == "x":
                    self.x = m
                elif l == "y":
                    self.y = m

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        to_dict = {}
        to_dict["id"] = self.id
        to_dict["width"] = self.width
        to_dict["height"] = self.height
        to_dict["x"] = self.x
        to_dict["y"] = self.y
        return to_dict

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
