#!/usr/bin/python3
"""Student to disk and reload"""
class Student:
    """Defines student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            results = {}
            for key in attrs:
                if hasattr(self, key):
                    results[key] = getattr(self, key)
            return results
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance:
        You can assume json will always be a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
