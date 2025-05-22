#!/usr/bin/python3
"""Only by 2"""
def divisible_by_2(my_list=[]):
    """Returns a list of True/False indicating if elements in the list
    are divisible by 2."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
