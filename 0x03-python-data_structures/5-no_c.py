#!/usr/bin/python3
""" Can you C me now?"""
def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string."""
    new_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
