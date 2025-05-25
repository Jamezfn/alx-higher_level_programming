#!/usr/bin/python3
"""Best score"""
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    best = None
    max_Val = None
    for key, value in a_dictionary.items():
        if max_Val is None or value > max_Val:
            max_Val = value
            best = key
    return key
