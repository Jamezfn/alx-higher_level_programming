#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Describes a class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute area of the class"""
        return self.__width * self.__height

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
