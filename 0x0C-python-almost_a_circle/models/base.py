#!/usr/bin/python3

"""sample module."""

import json
from os.path import exists
import csv
import turtle
import time
from random import random


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base object."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or type(list_dictionaries) is not list or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        name = cls.__name__
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(name + ".json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or type(json_string) is not str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance from a dictionary of attributes."""
        name = cls.__name__
        if name == "Rectangle":
            tmp = cls(1, 1)
        elif name == "Square":
            tmp = cls(1)
        else:
            tmp = None
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a JSON file."""
        name = cls.__name__ + ".json"
        if not exists(name):
            return []
        with open(name, "r+", encoding="utf-8") as file:
            tmp = cls.from_json_string(file.read())
        obj_list = []
        for item in tmp:
            obj_list.append(cls.create(**item))
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file."""
        name = cls.__name__
        obj_list = []
        if list_objs is not None:
            if name == "Rectangle":
                for obj in list_objs:
                    obj_list.append([obj.id, obj.width, obj.height, obj.x, obj.y])
            else:
                for obj in list_objs:
                    obj_list.append([obj.id, obj.size, obj.x, obj.y])
        with open(name + ".csv", "w+", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(obj_list)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file."""
        name = cls.__name__
        if not exists(name + ".csv"):
            return []
        with open(name + ".csv", "r+", encoding="utf-8", newline='') as file:
            reader = csv.reader(file)
            obj_list = []
            for row in reader:
                row = [int(i) for i in row]
                if name == "Rectangle":
                    attributes = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}
                elif name == "Square":
                    attributes = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                else:
                    return []
                obj_list.append(cls.create(**attributes))
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module."""
        shapes = list_rectangles + list_squares
        for shape in shapes:
            draw = turtle.Turtle()
            draw.color(random(), random(), random())
            draw.setpos(-shape.x, -shape.y)
            draw.pensize(7)
            draw.pendown()
            draw.forward(shape.width)
            draw.right(90)
            draw.forward(shape.height)
            draw.right(90)
            draw.forward(shape.width)
            draw.right(90)
            draw.forward(shape.height)
            draw.right(90)
            draw.end_fill()

        time.sleep(10)
