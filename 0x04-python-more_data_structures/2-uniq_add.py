#!/usr/bin/python3
"""Unique addition"""
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    new_int = set(my_list)
    total = 0
    for num in new_int:
        total += num
    return total
