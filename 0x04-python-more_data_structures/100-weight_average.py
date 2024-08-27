#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of all 
    integers tuple (<score>, <weight>)
    """
    return sum([x[0] * x[1] for x in my_list]) / \
            sum([x[1] for x in my_list] or 1)
