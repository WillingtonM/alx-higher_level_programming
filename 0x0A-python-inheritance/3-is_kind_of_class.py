#!/usr/bin/python3
"""Module containing is_kind_of_class method"""

def is_kind_of_class(obj, a_class):
    """is_kind_of_class returns true if object is instance of class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
