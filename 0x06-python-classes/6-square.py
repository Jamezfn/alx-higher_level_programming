#!/usr/bin/python3
"""Coordinates of a square"""
class Square:
    """Defines a square"""
    def __init__(self, size=0, position = (0, 0)):
        """Initialize square instance"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size attribute to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position attribute to a value"""
        if (not isinstance(value, tuple) or
        not isinstance(value, int) or
        len(value) != 2 or
        not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes area of the square instance"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)
