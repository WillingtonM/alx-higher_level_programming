#!/usr/bin/python3
"""Contains matrix_mul function"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers or floats)"""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not all(type(row) == list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if not all(type(m_row) == list for m_row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    m_row_len = len(m_a[0])
    if not all(len(m_row) == m_row_len for m_row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(type(m_numb) in [int, float] for m_row in m_a for m_numb in m_row):
        raise TypeError("m_a should contain only integers or floats")
    m_row_len = len(m_b[0])
    if not all(len(m_row) == m_row_len for m_row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not all(type(m_numb) in [int, float] for m_row in m_b for m_numb in m_row):
        raise TypeError("m_b should contain only integers or floats")
    a_cols = len(m_a[0])
    a_rows = len(m_a)
    b_rows = len(m_b)
    b_cols = len(m_b[0])
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    prod = [[0 for i in range(b_cols)] for j in range(a_rows)]
    for row_x in range(len(m_a)):
        col_b = 0
        while (col_b < b_cols):
            sum = 0
            for col_x in range(len(m_a[row_x])):
                sum += m_a[row_x][col_x] * m_b[col_x][col_b]
            prod[row_x][col_b] = sum
            col_b += 1
    return prod
