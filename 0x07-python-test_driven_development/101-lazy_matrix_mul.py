#!/usr/bin/python3

"""module to define matrix multiplier"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a is [[]]:
        raise ValueError("m_a can't be empty")

    if m_b is [[]]:
        raise ValueError("m_b can't be empty")

    lenn = len(m_a[0])

    for row in m_a:
        if lenn != len(row):
            raise TypeError("each row of m_a must be of the same size")
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_a should contain only integers or floats")
    
    lenn = len(m_b[0])

    for row in m_b:
        if lenn != len(row):
            raise TypeError("each row of m_b must be of the same size")
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)
