#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    pre_value = 0
    for char in reversed(roman_string):
        current_value = roman_to_int_map[char]
        if current_value < pre_value:
            total -= current_value
        else:
            total += current_value
    return total
