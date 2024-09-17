#!/usr/bin/python3
"""Class Student"""


class Student:
    """Attributes first, last, age
    method that retrieve dictionary representation of Student
    If attrs is a list of strings
    only attribute names contained in this list must be retrieved
    method that replaces all attributes of the Student instance:"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for x in range(len(attrs)):
                for y in obj:
                    if attrs[x] == y:
                        d_list[y] = obj[y]
            return d_list

        return obj

    def reload_from_json(self, json):
        for attr in json:
            self.__dict__[attr] = json[attr]
