#!/usr/bin/python3
"""Safe printing of an integers list"""
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
