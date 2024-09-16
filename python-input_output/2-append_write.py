#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
returns the number of characters added"""


def append_write(filename="", text=""):
    """appends string to end of file
    return characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
