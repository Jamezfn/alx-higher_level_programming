#!/usr/bin/python3
"""To uppercase"""
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end='')
    print()
