#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
from os.path import exists
import time
from random import random


class Base:
    """Base class for other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of the class from a dictionary."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a JSON file."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file."""
        name = cls.__name__
        ls = []
        if list_objs is not None:
            if name == "Rectangle":
                for a in list_objs:
                    ls.append([a.id, a.width, a.height, a.x, a.y])
            else:
                for a in list_objs:
                    ls.append([a.id, a.size, a.x, a.y])
        with open(name + ".csv", "w+", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file."""
        name = cls.__name__
        if not exists(name + ".csv"):
            return []
        with open(name + ".csv", "r+", encoding="utf-8", newline='') as file:
            tmp = csv.reader(file)
            ls = []
            for a in tmp:
                a = [int(i) for i in a]
                if name == "Rectangle":
                    dic = {"id": a[0], "width": a[1], "height": a[2],
                           "x": a[3], "y": a[4]}
                elif name == "Square":
                    dic = {"id": a[0], "size": a[1], "x": a[2], "y": a[3]}
                else:
                    return []
                ls.append(cls.create(**dic))
        return ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module."""
        shapes = list_rectangles + list_squares
        for a in shapes:
            draw = turtle.Turtle()
            draw.color(random(), random(), random())
            draw.setpos(-a.x, -a.y)
            draw.pensize(7)
            draw.pendown()
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.forward(a.width)
            draw.right(90)
            draw.forward(a.height)
            draw.right(90)
            draw.end_fill()

        time.sleep(10)
