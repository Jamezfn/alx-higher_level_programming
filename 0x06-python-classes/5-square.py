#!/usr/bin/python3
"""Printing a square"""
class Square:
    """Defines a Square class"""
    def __init__(self, size=0):
        """Initialize square instance"""
        self.__size = size

    @property
    def size(self):
        """Get size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Retrieve size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes area of the instance"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with character #"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
