#!/usr/bin/python3
"""Low memory cost"""
class LockedClass:
    """Prevents creating any new instance attributes except 'first_name'."""
    __slot__ = ['first_name']
