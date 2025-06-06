#!/usr/bin/python3
"""Area of a square"""
class Square:
    """Defines a square"""
    def __init__(self, size):
        """Initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square instance"""
        return self.__size ** 2
