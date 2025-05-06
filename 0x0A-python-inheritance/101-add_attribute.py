#!/usr/bin/python3
"""Class inheritance"""
def add_attribute(obj, attr_bute, value):
    """Attribute to an object if it’s possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_bute, value)
