#!/usr/bin/python3
"""This function prints "My name is <first name> <last name>" with user inputted names."""

def say_my_name(first_name, last_name=""):
	"""first_name and last_name must be a string"""
	if type(first_name) is not str:
		raise TypeError("first_name must be a string")
	if type(last_name) is not str:
		raise TypeError("last_name must be a string")
	else:
		print("My name is {} {}".format (first_name, last_name))
