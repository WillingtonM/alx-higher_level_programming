#!/usr/bin/python3
"""module for inspecting an object."""

def inherits_from(obj, a_class):
    """
    Checks if object inherited from specified class.

    Args:
        obj (any): Object to be checked.
        a_class (any): Class to be compared against.
    Returns:
        bool: True if `obj` is inheritance of `a_class`.
    """
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
