#!/usr/bin/python3
"""Define function that reads from a text file and prints it"""


def read_file(filename=""):
    """reads text file and prints it"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')