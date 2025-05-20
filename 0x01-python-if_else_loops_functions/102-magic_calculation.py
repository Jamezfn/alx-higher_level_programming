#!/usr/bin/python3
"""ByteCode -> Python #2"""
def magic_calculation(a, b, c):
    """Python bytecode"""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c


print(magic_calculation(1, 2, 3))
print(magic_calculation(3, 2, 1))
print(magic_calculation(4, 2, 3))
