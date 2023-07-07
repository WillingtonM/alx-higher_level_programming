#!/usr/bin/python3
"""Defines integer addition function."""

def add_integer(a, b=98):
    """Return integer addition of a and b.

    Raises:
        TypeError: If either of a / b is non-integer & non-float.
    """
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    return (int(b) + int(a))
