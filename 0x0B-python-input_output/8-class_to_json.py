#!/usr/bin/python3
"""Class to JSON"""
def class_to_json(obj):
    """Returns a dictionary description with a simple data structure"""
    return obj.__dict__
