#!/usr/bin/python3
"""Test-driven development"""
def add_integer(a, b=98):
    """Adds 2 integers.
        Args: a (int or float): First number.
              b (int or float, default=98): Second number.
        Returns: int: Sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
