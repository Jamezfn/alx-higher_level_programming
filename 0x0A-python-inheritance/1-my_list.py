#!/usr/bin/python3
"""My list"""
class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        return print(sorted(self))
