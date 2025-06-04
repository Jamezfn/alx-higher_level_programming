#!/usr/bin/python3
"""Area and Perimeter"""
class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initialise an instance"""
        self.width = width
        self.height = height

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
        """Return string representation using print_symbol for printing."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([self.print_symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string that can recreate the instance with eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement the counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
