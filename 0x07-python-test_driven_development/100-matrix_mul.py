#!/usr/bin/python3

"""module to define matrix multiplier"""

def matrix_mul(m_a, m_b):
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
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_a should contain only integers or floats")
