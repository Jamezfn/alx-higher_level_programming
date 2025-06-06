#!/usr/bin/python3
"""Read file"""
def read_file(filename=""):
    """Reads a text file and prints in to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
