#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass

    print()
    return count
