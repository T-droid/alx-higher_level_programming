#!/usr/bin/python3

"""module to define a pascal function"""


def pascal_triangle(n):
    """returns a list of lists of pascal triangle
    Args:
        n(int): represent a pascal triangle
    """
    if n <= 0:
        return []
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows

