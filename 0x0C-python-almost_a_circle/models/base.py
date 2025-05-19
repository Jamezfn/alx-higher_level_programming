#!/usr/bin/python3
"""Base class"""
import json
import os
import csv
import turtle
class Base:
    """Defining a base class module"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None and len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
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
        """Returns the list of the JSON string representation json_string"""
        if json_string is None and len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            json_str = f.read()
        list_dict = cls.from_json_string(json_str)
        return [cls.create(**d) for d in list_dict]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is None or len(list_objs) == 0:
                return
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Writes the CSV string representation of list_objs to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            instances = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj_dict = {"id" : int(row[0]), "width" : int(row[1]), "height" : int(row[2]), "x" : int(row[3]), "y" : int(row[4])}
                elif cls.__name__ == "Square":
                     obj_dict = {"id" : int(row[0]), "size" : int(row[1]), "x" : int(row[2]), "y" : int(row[3])}
                instance = cls.create(**obj_dict)
                instances.append(instance)
            return instances
    
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.
        """
        screen = turtle.Screen()
        screen.title("Shapes Drawing")
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(2)
        pen.pensize(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for sq in list_squares:
            pen.penup()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(sq.size)
                pen.left(90)

        pen.hideturtle()
        screen.mainloop()
