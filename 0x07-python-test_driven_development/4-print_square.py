#!/usr/bin/python3
"""Defines square-printing function."""


def print_square(size):
    """Print square with the # character.

    Args:
        size: The height or width of square.
    Raises:
        TypeError: If size is not integer.
        ValueError: If size is is less than 0
    """
    err_1 = "size must be an integer"
    err_2 = "size must be >= 0"
    if not isinstance(size, int):
        raise TypeError(err_1)
    if size < 0:
        raise ValueError(err_2)

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
