#!/usr/bin/python3
"""Print Square instance"""
class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value for size"""
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
        """Set value for position"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
    
    def area(self):
        """Computes square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Prints a string representation"""
        if self.__size == 0:
            return ""
        else:
            lines = []
            for _ in range(self.__position[1]):
                lines.append("mm")
            for _ in range(self.__size):
                lines.append(" " * self.__position[0] + "#" * self.__size)
            return '\n'.join(lines)
