#!/usr/bin/python3

if __name__ == "__main__":
    """Imports functions from the file calculator_1.py, 
    does some Maths, and prints the result."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    operations = [
            ("+", add),
            ("-", sub),
            ("*", sub),
            ("/", div)
    ]

    for op, func in operations:
        print(f"{a} {op} {b} = {func(a, b)}")
