#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
from os.path import exists
import turtle
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
    def to_json_string(list_of_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_of_dictionaries is None or list_of_dictionaries == []:
            return "[]"
        return json.dumps(list_of_dictionaries)

    @classmethod
    def save_to_file(cls, list_of_objects):
        """Save a list of objects to a JSON file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_of_objects is None:
                json_file.write("[]")
            else:
                list_of_dicts = [o.to_dictionary() for o in list_of_objects]
                json_file.write(Base.to_json_string(list_of_dicts))

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
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a JSON file."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_of_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objects):
        """Save a list of objects to a CSV file."""
        name = cls.__name__
        data = []
        if list_of_objects is not None:
            if name == "Rectangle":
                for obj in list_of_objects:
                    data.append([obj.id, obj.width, obj.height, obj.x, obj.y])
            else:
                for obj in list_of_objects:
                    data.append([obj.id, obj.size, obj.x, obj.y])
        with open(name + ".csv", "w+", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file."""
        name = cls.__name__
        if not exists(name + ".csv"):
            return []
        with open(name + ".csv", "r+", encoding="utf-8", newline='') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                row = [int(i) for i in row]
                if name == "Rectangle":
                    dictionary = {"id": row[0], "width": row[1], "height": row[2],
                           "x": row[3], "y": row[4]}
                elif name == "Square":
                    dictionary = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                else:
                    return []
                data.append(cls.create(**dictionary))
        return data

    @staticmethod
    def draw(list_of_rectangles, list_of_squares):
        """Draw rectangles and squares using the turtle module."""
        shapes = list_of_rectangles + list_of_squares
        for shape in shapes:
            draw_turtle = turtle.Turtle()
            draw_turtle.color(random(), random(), random())
            draw_turtle.setpos(-shape.x, -shape.y)
            draw_turtle.pensize(7)
            draw_turtle.pendown()
            draw_turtle.forward(shape.width)
            draw_turtle.right(90)
            draw_turtle.forward(shape.height)
            draw_turtle.right(90)
            draw_turtle.forward(shape.width)
            draw_turtle.right(90)
            draw_turtle.forward(shape.height)
            draw_turtle.right(90)
            draw_turtle.end_fill()

        time.sleep(10)
