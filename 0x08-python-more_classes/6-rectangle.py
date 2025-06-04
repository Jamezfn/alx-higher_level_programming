#!/usr/bin/python3
"""Area and Perimeter"""
class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialise an instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width for the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute area of the Rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print rint the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """String representation of the rectangle to be able to 
        recreate a new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Decrement instance count and print a message on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
