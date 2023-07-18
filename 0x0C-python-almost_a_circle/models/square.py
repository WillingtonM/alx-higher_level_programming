#!/usr/bin/python3
"""Defines square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialize a new Square.

            Args:
                size (int): Size of new Square.
                x (int): x coordinate of new Square.
                y (int): y coordinate of new Square.
                id (int): Identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set or get size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Update Square.

            Args:
                *args (ints): New attribute values.
                    - 1st arg represents id attribute
                    - 2nd arg represents size attribute
                    - 3rd arg represents x attribute
                **kwargs (dict): New key/value pairs of attributes.
                    - 4th arg represents y attribute
        """
        if args and len(args) != 0:
            ag = 0
            for arg in args:
                if ag == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ag == 1:
                    self.size = arg
                elif ag == 2:
                    self.x = arg
                elif ag == 3:
                    self.y = arg
                ag += 1

        elif kwargs and len(kwargs) != 0:
            for l, m in kwargs.items():
                if l == "id":
                    if m is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = m
                elif l == "size":
                    self.size = m
                elif l == "x":
                    self.x = m
                elif l == "y":
                    self.y = m

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        to_dict = {}
        to_dict["id"] = self.id
        to_dict["size"] = self.size
        to_dict["x"] = self.x
        to_dict["y"] = self.y
        return to_dict

    def __str__(self):
        """Return print() and str() representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
