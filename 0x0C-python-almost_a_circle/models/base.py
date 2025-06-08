#!/usr/bin/python3
"""Base class"""
import json
import os
import csv
class Base:
    """Base of all classes"""
    __nb_objects =0
    def __init__(self, id=None):
        """instance initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_str = cls.to_json_string(list_dicts)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
         
        """Returns an instance with all attrinutes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
        list_dicts = cls.from_json_string(contents)
        instances = [cls.create(**d) for d in list_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to csv file"""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == 'Square':
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])


    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from csv file"""
        filename = f"{cls.__name__}.csv"
        if not os.path.isfile(filename):
            return []
        instances = []
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row = list(map(int, row))
                if cls.__name__ == 'Rectangle':
                    keys = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == 'Square':
                    keys = ["id", "size", "x", "y"]
                else:
                    continue
                dictionary = dict(zip(keys, row))
                instances.append(cls.create(**dictionary))
        return instances
