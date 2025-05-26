#!/usr/bin/python3
"""ByteCode -> Python #4"""
def magic_calculation(a, b):
    """ByteCode"""
    result = 
    for i in range(103):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
