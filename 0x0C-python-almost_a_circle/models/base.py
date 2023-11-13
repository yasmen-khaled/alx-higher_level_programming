#!/usr/bin/python3

"""Defines a base model class."""
import json

class BaseModel:
    """BaseModel class"""

    __object_count = 0

    def __init__(self, identity=None):
        """Initialize a new BaseModel."""
        if identity is not None:
            self.identity = identity
        else:
            BaseModel.__object_count += 1
            self.identity = BaseModel.__object_count

    @staticmethod
    def to_json_string(dict_list):
        """Convert list of dictionaries to JSON string."""
        if dict_list is None or dict_list == []:
            return "[]"
        return json.dumps(dict_list)

    @classmethod
    def save_to_file(cls, object_list):
        """Save list of objects to a JSON file."""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if object_list is None:
                json_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in object_list]
                json_file.write(BaseModel.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_str):
       """Convert JSON string to list."""
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attributes):
        """Create a new instance from a dictionary of attributes."""
        if attributes and attributes != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**attributes)
            return new_instance

    @classmethod
    def load_from_file(cls):
      """Load list of objects from a JSON file."""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as json_file:
                dict_list = BaseModel.from_json_string(json_file.read())
                return [cls.create(**dict) for dict in dict_list]
        except IOError:
            return []
