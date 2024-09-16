#!/usr/bin/python3
"""Class Student"""


class Student:
    """Attributes first, last, age
    method that retrieve dictionary representation of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary method"""
        return self.__dict__
