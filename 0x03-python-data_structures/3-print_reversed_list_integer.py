#!/usr/bin/python3
"""Print a list of integers... in reverse!"""
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
