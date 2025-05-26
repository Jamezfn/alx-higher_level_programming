#!/usr/bin/python3
"""Safe integer print with error message"""
def safe_print_integer_err(value):
    """Prints an integer."""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=__import__('sys').stderr)
        return False
