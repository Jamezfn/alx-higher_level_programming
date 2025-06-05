#!/usr/bin/python3
"""Integer validator"""
class BaseGeometry:
    """Integer validator"""
    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
