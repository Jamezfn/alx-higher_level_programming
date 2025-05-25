#!/usr/bin/python3
"""Search and replace"""
def search_replace(my_list, search, replace):
    """Returns a new list where all occurrences 
    of 'search' in 'my_list' are replaced with 'replace'."""
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
