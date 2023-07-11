#!/usr/bin/python3
"""Rectangle class Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry """

    def __init__(self, width, height):
        """Initialise a new Rectangle.
        Args:
            width (int): Width of new Rectangle instance
            height (int): Height of new Rectangle instance
        """
        self.integer_validator('height', height)
        self.__height = height
        self.integer_validator('width', width)
        self.__width = width
