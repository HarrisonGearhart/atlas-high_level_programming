#!/usr/bin/python3
"""Checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Checks if object type is a_class
    if so, Returns true if is instance of a class is inherented
    false otherwise"""
        if type(object) != a_class:
            return issubclass(type(opject), a_class)
        else:
            return False
