#!/usr/bin/python3
"""This function that prints a square with the character #."""

def print_square(size):
	"""size must be an integer
	if size < 0, raise error
	if size if float and less than 0, type error"""
	if type(size) is not int:
		raise TypeError("size must be an integer")
	if size < 0:
		raise TypeError("size must be >= 0")
	if type(size) is float and size < 0:
		raise TypeError("size must be an integer")
	for i in range(size):
		print("{}".format("#") * size)
