#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list[1:]:
        if num > max_value:
            max_value = num 
    return max_value
