#!/usr/bin/python3
"""Rectangle class Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method
        Args:
            width (int): Width of new Rectangle instance
            height (int): Height of new Rectangle instance
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
