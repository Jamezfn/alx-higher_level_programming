#!/usr/bin/python3
"""Eval is magic"""
class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize an instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width for instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve instance width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes area of the instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the Rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation that can be used to recreate the instance
        with eval(): "Rectangle(width, height)"."""
        return f"Rectangle({self.__width}, {self.__height})"
