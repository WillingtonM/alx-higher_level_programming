#!/usr/bin/python3
"""
Dividing list of list of int and float by divisor
"""


def matrix_divided(matrix, div):
    """divide through by mtrix

    Args:
        matrix: List of list of int or float
        div: Divisor

    Raises:
        Typerror: If matrix is not list of list
        Typerror: If matrix contain anthing other than int & float
        Typerror: If div not a number is 0
        Typerror: If matrix is not regular

    Returns:
        New list without mutatng original list
    """
    err_1 = "matrix must be a matrix (list of lists)\of integers/floats"
    err_2 = "Each row of the matrix must have the same size"
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(numb, list) for numb in matrix)
        or not all((isinstance(element, int))
                   or (isinstance(element, float))
                   for element in [i for j in matrix for i in j])):
        raise TypeError(err_1)
    if not (all( len(matrix[0]) == len(y) for y in matrix)):
        raise TypeError(err_2)
    if not ( (isinstance(div, float)) or (isinstance(div, int))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return ([list(map((lambda z: round(z / div, 2)), row)) for row in matrix])
