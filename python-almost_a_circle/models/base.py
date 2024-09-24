#!/usr/bin/python3
"""Base Class Model"""
import json


class Base:
    """Base model for all other classes
    __nb_onjects attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of a list of dicts.
        args - list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects
        args - lists_objs (list of inherited Base instances)
        """
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for li5t in list_objs:
                text.append(li5t.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        json_string is a string representing a list of dictionaries
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
