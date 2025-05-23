#!/usr/bin/python3
"""Class to JSON"""

def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) 
    for JSON serialization of an object."""
    obj_desc = obj.__dict__
    return obj_desc
