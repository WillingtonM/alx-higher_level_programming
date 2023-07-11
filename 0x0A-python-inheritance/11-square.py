#!/usr/bin/python3
"""Square class Module"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """extends class Rectangle
    """
    def __init__(self, size):
        """initializes all instances of Square
            Args:
                size(int): size of square
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Area of Square
        """
        return self.__size ** 2

    def __str__(self):
        """Description of square
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
