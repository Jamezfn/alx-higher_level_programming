#!/usr/bin/python3
"""Square #2"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Describes a square class inheriting from Rectangle"""
    def __init__(self, size):
        """Initialize a Square by validating size and calling Rectangle initializer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Print a string representation of the square class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
