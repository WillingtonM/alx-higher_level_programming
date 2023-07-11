#!/usr/bin/python3
"""Module containing add_attribute method"""

def add_attribute(cls, name, value):
    """adds new attribute if possible.
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
