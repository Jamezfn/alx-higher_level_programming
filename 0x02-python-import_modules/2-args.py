#!/usr/bin/python3
"""How to make a script dynamic!"""
if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
