#!/usr/bin/python3
"""returns True if the object is an instance of
or if the object is an instance of a class that inherited from
otherwise False."""


def is_kind_of_class(obj, a_class):
    """True or False return"""
    return isinstance(obj, a_class)
