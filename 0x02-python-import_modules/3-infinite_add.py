#!/usr/bin/python3
"""Infinite addition"""
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    import sys
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)
