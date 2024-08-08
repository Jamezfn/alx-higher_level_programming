#!/usr/bin/python3
def remove_char_at(str, n):
    """Remove the character at index n from the string str."""
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    else:
        return str
