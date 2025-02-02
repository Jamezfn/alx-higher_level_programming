#!/usr/bin/python3
"""Classes and Objects"""

class Square:
     """A class that defines a square."""
     def __init__(self, size=0, position=(0, 0)):
         """Initialize the square with a private size attribute."""
         self.size = size
         self.position = position

     @property
     def size(self):
         """Get the size of the square."""
         return self.__size

     @property
     def position(self):
         """Retrieve the position of the square."""
         return self.__position

     @size.setter
     def size(self, value):
         """Set the size of the square, ensuring it is a non-negative integer."""
         if not isinstance(value, int):
             raise TypeError("size must be an integer")
         if value < 0:
             raise ValueError("size must be >= 0")
         self.__size = value

     @position.setter
     def position(self, value):
         """Set the position of the square with validation."""
         if not isinstance(value, tuple) or \
            not all(isinstance(num, int) for num in value) or \
            not all(num >= 0 for num in value):
                raise TypeError("position must be a tuple of 2 positive integers")
         self.__position = value

     def area(self):
         """Return area of the square."""
         return self.__size ** 2

     def my_print(self):
         """Print the square using '#' characters or an empty line if size is 0."""
         if self.__size < 0:
             print()
             return
         for _ in range(self.__position[1]):
             print()
         for _ in range(self.__size):
             print(" " * self.__position[0] + "#" * self.__size)

     def __str__(self):
         """Return a string representation of the square, behaving like my_print()."""
         result = []
         if self.__size == 0:
             return ""

         for _ in range(self.__position[1]):
             result.append("")
         for _ in range(self.__size):
             result.append(" " * self.__position[0] + "#" * self.__size)

         return "\n".join(result)
