#!/usr/bin/python3
"""Defines function that checks if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns true or false if it is the same class or not"""
    return type(obj) == a_class
