#!/usr/bin/python3
"""There are only 3 colors, 10 digits, and 7 notes"""
def print_last_digit(number):
    """Prints the last digit of a number."""
    digit = abs(number) % 10
    print("{}".format(digit), end='')
    return digit
