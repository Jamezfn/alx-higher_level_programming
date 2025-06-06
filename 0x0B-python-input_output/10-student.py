#!/usr/bin/python3
"""Student to JSON"""
class Student:
    """Describes a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialise a class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of the instance"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__.copy()
