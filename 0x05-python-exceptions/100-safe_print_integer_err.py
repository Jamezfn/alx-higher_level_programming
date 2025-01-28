#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer."""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
