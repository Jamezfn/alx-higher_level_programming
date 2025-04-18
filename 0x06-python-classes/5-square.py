#!/usr/bin/python3
"""Classes and Objects"""

class Square:
     """A class that defines a square."""
     def __init__(self, size):
         """Initialize the square with a private size attribute."""
         self.size = size

     @property
     def size(self):
         """Get the size of the square."""
         return self.__size

     @size.setter
     def size(self, value):
         """Set the size of the square, ensuring it is a non-negative integer."""
         if not isinstance(value, int):
             raise TypeError("size must be an integer")
         if value < 0:
             raise ValueError("size must be >= 0")
         self.__size = value

     def area(self):
         """Return area of the square."""
         return self.__size ** 2

     def my_print(self):
         """Print the square using '#' characters or an empty line if size is 0."""
         if self.__size < 0:
             print()
         else:
             for _ in range(self.__size):
                 print("#" * self.__size)

