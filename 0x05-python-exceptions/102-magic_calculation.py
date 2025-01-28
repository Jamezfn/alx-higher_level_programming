#!/usr/bin/python3

def magic_calculation(a, b):
    """Python bytecode"""
    result = 0
    for i in the range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break

    return result
