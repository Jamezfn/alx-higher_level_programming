#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    """
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] is value:
            del a_dictionary[x]
    return a_dictionary
