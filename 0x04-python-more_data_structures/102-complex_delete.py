#!/usr/bin/python3
"""Delete by value"""
def complex_delete(a_dictionary, value):
    key_remove = [k for k, v in a_dictionary.items() if v == value]
    for key in key_remove:
        del a_dictionary[key]
    return a_dictionary
