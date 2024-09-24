#!/usr/bin/python3
"""Base Class Model"""


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
