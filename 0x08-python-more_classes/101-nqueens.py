#!/usr/bin/python3
"""N queens"""
import sys
class NQueenSolver:
    """Validation and backtracking logic for solving N-Queens"""
    def __init__(self, n):
        """Instantiation"""

    @staticmethod
    def print_usage():
        """User called the program with the wrong number of arguments"""
        print("Usage: nqueens N")
        sys.exit(1)

    @staticmethod
    def valid_args():
        """Minimum number of arguments"""
        print("N must be a number")
        sys.exit(1)
    
    @staticmethod
    def min_int():
        print("N must be at least 4")
        sys.exit(1)

    def solutions(n):
        """Finds all posible solutions"""

def main():
    """Root program"""
    if len(sys.argv) != 2:
        print_usage()

    arg = sys.argv[1]
    try:
        n = int(arg)
    except TypeError:
        valid_args()

    if n < 4:
        min_int()

if __name__ == '__main__':
    main()
