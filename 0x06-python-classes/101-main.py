#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (1, 2))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
