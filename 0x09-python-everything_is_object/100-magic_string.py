#!/usr/bin/python3
def magic_string():
    """#pythonic"""
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "BestSchool" * magic_string.count if magic_string.count == 1 else ", ".join(["BestSchool"] * magic_string.count)
