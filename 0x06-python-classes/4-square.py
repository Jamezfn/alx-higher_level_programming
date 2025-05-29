#!/usr/bin/python3
"""Access and update private attribute"""
class Square:
    """Defines square"""
    def __init__(self, size):
        """initialization"""
        self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes area of square"""
        return self.__size ** 2
