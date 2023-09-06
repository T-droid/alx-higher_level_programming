#!/usr/bin/python3

"""module for matrix division"""
def matrix_divided(matrix, div):
    """function to divide a matrix
    Args:
        matrix(list): the matrix
        div(int): number to divide the matrix
    """
    if not isinstance(matrix, list) and not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lent = len(matrix[0])

    for row in matrix:
        if len(row) != lent:
            raise TypeError("Each row of matrix must have the same size")

        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
