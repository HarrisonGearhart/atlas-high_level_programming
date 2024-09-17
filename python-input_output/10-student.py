#!/usr/bin/python3
"""Class Student"""


class Student:
    """Attributes first, last, age
    method that retrieve dictionary representation of Student
	If attrs is a list of strings
	only attribute names contained in this list must be retrieved."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

	def to_json(self, attrs=None):
		if type(attrs) is list:
			for item in attrs:
				if type(item) is not str:
					return obj
	