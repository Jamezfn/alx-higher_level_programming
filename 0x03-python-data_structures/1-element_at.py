#!/usr/bin/python3
"""Secure access to an element in a list"""
def element_at(my_list, idx):
    """Retrieves an element from a list like in C."""
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
