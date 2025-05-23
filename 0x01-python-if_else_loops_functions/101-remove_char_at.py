#!/usr/bin/python3
"""Remove at position"""
def remove_char_at(str, n):
    """Removes a character at the position n"""
    if n < 0 or n > len(str):
        return str
    return str[:n] + str[n+1:]
