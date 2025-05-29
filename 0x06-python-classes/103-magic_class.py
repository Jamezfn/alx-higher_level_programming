#!/usr/bin/python3
"""ByteCode -> Python #5"""
from math import pi
class MagicClass:
    """ByteCode"""
    def __init__(self, radius=0):
        """Initialisation"""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes area of the circle"""
        return pi * self.__radius ** 2

    def circumference(self):
        """Computes circumference of the circle"""
        return 2 * pi * self.__radius
