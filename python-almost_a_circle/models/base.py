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
        with open(filename, "w") as jsonfile:
            if lists_objs is None:
                jsonfile.write("[]")
            else:
                lists_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
