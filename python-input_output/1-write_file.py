#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
returns the number of characters written"""


def write_file(filename="", text=""):
    """writes string to text file
    returns number of characters written"""
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
