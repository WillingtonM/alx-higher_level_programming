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
    err_1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_2 = "Each row of the matrix must have the same size"

    if(not isinstance(matrix,list) or not len(matrix) or
       0 in [len(listx) if type(listx) is list else 0 for listx in matrix] or
       any(False in i for i in  [[isinstance(elemnt,(int,float)) for elemnt in row]
       for row in matrix])):
        raise TypeError(err_1)
    if(len(set([len(listx) for listx in matrix])) > 1):
        raise TypeError(err_2)
    if(not isinstance(div,(int,float))):
        raise TypeError('div must be a number')
    if(div is 0):
        raise ZeroDivisionError('division by zero')
    return [[round(elemnt / div, 2) for elemnt in row] for row in matrix]
