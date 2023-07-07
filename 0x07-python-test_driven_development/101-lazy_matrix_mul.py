#!/usr/bin/python3
"""
This program takes two matrices and multiply them with the library numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices with numpy
      Args:
        m_a (int or float): list of lists
        m_b (int or float): list of lists
    """
    return np.matmul(m_a, m_b)
