#!/usr/bin/python3
"""Import a simple function from a simple file"""
from add_0 import add
if __name__ == "__main__":
    """Imports a function then prints the results"""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
