#!/usr/bin/python3
"""Module containing is_same_class method"""

def is_same_class(obj, a_class):
    """ is_same_class returns True if object is an instance of specified class
        Returns: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
