#!/usr/bin/python3
"""Roman to Integer"""
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
    total = 0
    prev_value = 0
    for char in roman_string[::-1]:
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total
