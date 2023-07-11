#!/usr/bin/python3
"""Abject attribute lookup method."""

def lookup(obj):
    """ lookup method
        Returns: List of available attributes and methods.
        Args:
            obj (object): object.
    """
    return (dir(obj))
