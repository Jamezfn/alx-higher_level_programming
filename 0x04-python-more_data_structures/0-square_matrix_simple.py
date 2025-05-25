#!/usr/bin/python3
"""Squared simple"""
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers in a 2D matrix."""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
