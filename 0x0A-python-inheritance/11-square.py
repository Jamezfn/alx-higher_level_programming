#!/usr/bin/python3
"""Class inheritance"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Square #2"""
    def __init__(self, size):
        """Initiallization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
