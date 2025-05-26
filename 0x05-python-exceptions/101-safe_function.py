#!/usr/bin/python3
"""Safe function"""
def safe_function(fct, *args):
    """Executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=__import__('sys').stderr)
        return None
