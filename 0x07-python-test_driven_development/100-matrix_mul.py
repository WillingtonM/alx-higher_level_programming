#!/usr/bin/python3
"""Contains the matrix_mul function
"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers or floats)"""
    err_1 = "each row of m_a must must be of the same size"
    err_2 = "m_a should contain only integers or floats"
    err_3 = "each row of m_b must should be of the same size"
    err_4 = "m_b should contain only integers or floats"
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elemnts in m_a:
        if not isinstance(elemnts, list):
            raise TypeError("m_a must be a list of lists")

    for elemnts in m_b:
        if not isinstance(elemnts, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for m_ls in m_a:
        for elemnts in m_ls:
            if not type(elemnts) in (int, float):
                raise TypeError(err_2)

    for m_ls in m_b:
        for elemnts in m_ls:
            if not type(elemnts) in (int, float):
                raise TypeError(err_4)

    m_len = 0
    for elemnts in m_a:
        if m_len != 0 and m_len != len(elemnts):
            raise TypeError(err_1)
        m_len = len(elemnts)

    m_len = 0
    for elemnts in m_b:
        if m_len != 0 and m_len != len(elemnts):
            raise TypeError("each row of m_b must be of the same size")
        m_len = len(elemnts)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row1 = []
    i1 = 0

    for b in m_a:
        row2 = []
        i_sum2 = 0
        sum_t = 0
        while (i_sum2 < len(m_b[0])):
            sum_t += b[i1] * m_b[i1][i_sum2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i_sum2 += 1
                row2.append(sum_t)
                sum_t = 0
            else:
                i1 += 1
        row1.append(row2)

    return row1