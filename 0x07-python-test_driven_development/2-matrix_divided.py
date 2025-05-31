#!/usr/bin/python3
"""Divide a matrix"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if not isinstance(matrix, list) or not matrix or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    first_len =len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2)for x in row] for row in matrix]
