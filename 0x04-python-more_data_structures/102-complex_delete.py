#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for i in keys_to_delete:
        del a_dictionary[i]
    return a_dictionary
