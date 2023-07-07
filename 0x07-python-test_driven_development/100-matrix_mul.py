#!/usr/bin/python3
"""Contains the matrix_mul function
"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers or floats)"""
    err_1 = "each row of m_a must should be of the same size"
    err_2 = "m_a should contain only integers or floats"
    err_3 = "each row of m_b must should be of the same size"
    err_4 = "m_b should contain only integers or floats"
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len_1 = len(m_a)
    if len_1 == 0:
        raise ValueError("m_a can't be empty")
    len_2 = None
    for r in m_a:
        if type(r) is not list:
            raise TypeError("m_a must be a list of lists")
        if len_2 is None:
            len_2 = len(r)
            if len_2 == 0:
                raise ValueError("m_a can't be empty")
        if len_2 != len(r):
            raise TypeError(err_1)
        for s in r:
            if type(s) is not int and type(s) is not float:
                raise TypeError(err_2)
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len_3 = None
    for c in m_b:
        if type(c) is not list:
            raise TypeError("m_b must be a list of lists")
        if len_3 is None:
            len_3 = len(c)
            if len_3 == 0:
                raise ValueError("m_b can't be empty")
        if len_3 != len(c):
            raise TypeError(err_3)
        for d in c:
            if type(d) is not int and type(d) is not float:
                raise TypeError(err_4)
    if len_2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = []
    for x in range(len_1):
        l = []
        for y in range(len_3):
            sum_t = 0
            for col_z in range(len_2):
                sum_t += m_a[x][col_z] * m_b[col_z][y]
            l.append(sum_t)
        product.append(l)
    return product