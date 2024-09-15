#!/usr/bin/python3
"""Class called MyList"""


class MyList(list):
    """initializes the list class
    define method that prints the list sorted in ascending order"""
    def print_sorted(self):
        print(sorted(self))
