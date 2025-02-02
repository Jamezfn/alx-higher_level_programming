#!/usr/bin/python3
"""ByteCode -> Python #5"""
import math
class MagicClass:
    """"""
    def __init__(self, radius=0):
        """A class that replicates the behavior of the provided bytecode."""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Retrieve the radius of the circle"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value < 0:
            return ValueError("radius must be >= 0")
        self.__radius = value

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius


# Create an instance of MagicClass
circle = MagicClass(5)

# Calculate and print the area
print("Area:", circle.area())

# Calculate and print the circumference
print("Circumference:", circle.circumference())

# Try setting an invalid radius
try:
    circle.radius = "invalid"
except TypeError as e:
    print(e)
