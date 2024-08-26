#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    return list(map(lambda x: list(map(lambda i: i**2, x)), matrix))
