#!/usr/bin/python3
"""Only differents"""
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    return set_1.symmetric_difference(set_2)
