#!/usr/bin/python3
"""Inheritance module"""

class MyList(list):
    """A class inheriting from list"""
    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
