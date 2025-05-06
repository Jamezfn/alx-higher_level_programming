#!/usr/bin/python3
"""Class inheritance"""
class MyInt(int):
    """My integer"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
