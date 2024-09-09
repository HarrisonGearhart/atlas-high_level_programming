#!/usr/bin/python3
"""This function adds two integers"""

def add_integer(a, b=98):
	"""if a or b isn't a float or integer, raise error
	cast floats into ints
	return a + b"""
	
	if type(a) not in [int, float]:
		raise TypeError("a must be an integer")
	if type(b) not in [int, float]:
		raise TypeError("b must be an integer")
	return int(a) + int(b)
