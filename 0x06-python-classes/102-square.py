#!/usr/bin/python3
"""Classes and Objects"""

class Square:
     """A class that defines a square."""
     def __init__(self, size=0):
         """Initialize the square with a private size attribute."""
         self.size = size

     @property
     def size(self):
         return self.__size
    
     @size.setter
     def size(self, size):
         """Set the size of the square, ensuring it is a non-negative integer."""
         if not isinstance(size, int):
             raise TypeError("size must be an integer")
         if size < 0:
             raise ValueError("size must be >= 0")
         self.__size = size

     def area(self):
         """Return area of the square"""
         return self.__size ** 2

     def __eq__(self, other):
         """Check if two squares have the same area."""
         return self.area() == other.area()

     def __ne__(self, other):
         """Check if two squares have different areas."""
         return self.area() != other.area()

     def __gt__(self, other):
         """Check if the area of the current square is greater than the other."""
         return self.area() > other.area()

     def __lt__(self, other):
         """Check if the area of the current square is less than the other."""
         return self.area() < other.area()

     def __le__(self, other):
         """Check if the area of the current square is less than or equal to the other."""
         return self.area() <= other.area()

     def __ge__(self, other):
         """Check if the area of the current square is 
         greater than or equal to the other."""
         return self.area() > other.area()
