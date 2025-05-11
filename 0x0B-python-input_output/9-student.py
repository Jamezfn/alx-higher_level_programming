#!/usr/bin/python3
"""Student to JSON"""
class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Class initiallization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        dict_rep = self.__dict__
        return dict_rep
