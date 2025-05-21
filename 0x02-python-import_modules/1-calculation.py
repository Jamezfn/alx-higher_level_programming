#!/usr/bin/python3
"""My first toolbox!"""
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    """Does some mathematics and prints them results"""
    a = 10
    b = 5

    operations = [
            ("+", add),
            ("-", sub),
            ("*", mul),
            ("/", div)
            ]
    for op, func in operations:
        print("{} {} {} = {}".format(a, op, b, func(a, b)))
