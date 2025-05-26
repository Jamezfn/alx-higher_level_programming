#!/usr/bin/python3
"""Integers division with debug"""
def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
