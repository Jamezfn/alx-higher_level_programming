#!/usr/bin/python3
"""Real definition of a rectangle"""

class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """initiallizing the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve Height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
