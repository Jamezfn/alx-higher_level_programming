#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Describes a square class that inherits from a triangle"""
    def __init__(self, size):
        """Initialize a Square by validating size and calling Rectangle initializer."""
        self.integer_validator("size", size)
        super().__init__(size, size)
