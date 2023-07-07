#!/usr/bin/python3
"""Defines a function that prints my name.

Attributes:
    say_my_name: Prints my name.
"""

def say_my_name(first_name, last_name=""):
    """Prints my name.

    Args:
        first_name: First name.
        last_name: Second name, Defaults to ''.

    Raises:
        TypeError: If either first name or last name is not string.
    """
    err_1 = "first_name must be a string"
    err_2 = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(err_1)

    if not isinstance(last_name, str):
        raise TypeError(err_2)

    print("My name is {} {}".format(first_name, last_name))
