#!/usr/bin/python3
"""Print a list of integers"""
def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
