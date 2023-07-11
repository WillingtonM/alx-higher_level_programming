#!/usr/bin/python3
"""Module for pascal_triangle method."""

def pascal_triangle(n):
    """
        returns list of lists of integers
        Args:
            n (int): Number of lists & digits
        Returns: list of lists
    """
    l_rows = [[1 for k in range(j + 1)] for j in range(n)]
    for n in range(n):
        for j in range(n - 1):
            l_rows[n][j + 1] = sum(l_rows[n - 1][j:j + 2])
    return l_rows

