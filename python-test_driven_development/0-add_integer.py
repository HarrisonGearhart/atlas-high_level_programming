#!/usr/bin/python3
"""This function adds two integers"""

def add_integer(a, b=98):
	"""if a or b isn't a float or integer, raise error
	cast floats into ints
	return a + b"""
	if a == float:
		a = int(a)
	if b == float:
		b = int(b)
	if a != int:
		raise TypeError("a must be an integer")
	if b != int:
		raise TypeError("b must be an integer")
	else:
		return a + b
