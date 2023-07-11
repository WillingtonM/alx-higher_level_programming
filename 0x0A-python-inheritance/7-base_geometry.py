#!/usr/bin/python3
"""BaseGeometry class Module"""

class BaseGeometry:
    """ BaseGeometry class
        Attributes: None.
        Methods:
            area() - raises an Exception
            integer_validator() - validates value.
    """
    def area(self):
        """ Method Raises Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            checks the value of value.
            Args:
                name (str): name
                value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
