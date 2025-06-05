#!/usr/bin/python3
"""My integer"""
class MyInt(int):
    """Describes a class that inverts == and != operators"""
    def __eq__(self, other):
        """Inverts equal to"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Inverts not equal to"""
        return not super().__ne__(other)
