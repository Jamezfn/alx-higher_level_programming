#!/usr/bin/python3
"""Student to JSON"""
class Student:
    """Describes a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialise a class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of the instance"""
        return self.__dict__
