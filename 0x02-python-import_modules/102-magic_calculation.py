#!/usr/bin/python3
"""ByteCode -> Python #3"""
def magic_calculation(a, b):
    """Python bytecode"""
    from magic_calculation_10 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
