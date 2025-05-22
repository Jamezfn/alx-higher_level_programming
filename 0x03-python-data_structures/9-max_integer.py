#!/usr/bin/python3
"""Find the max"""
def max_integer(my_list=[]):
    """Finds and returns the biggest integer in a list."""
    if len(my_list) == 0:
        return None
    big_int = my_list[0]
    for i in my_list[1:]:
        if i > big_int:
            big_int = i
    return big_int
