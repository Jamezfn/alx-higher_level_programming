#!/usr/bin/python3
"""Replace in a copy"""
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without 
    modifying the original list (like in C)."""
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list):
        return my_list
    else:
        new_list[idx] = element
        return new_list
