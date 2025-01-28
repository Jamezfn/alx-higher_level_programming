#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    """Function that executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exeption: {}".format(e), file=sys.stderr)
        return None
