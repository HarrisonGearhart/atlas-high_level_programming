#!/usr/bin/python3
"""This function adds two integers"""

def add_integer(a, b=98):
"""if a or b isn't a float or integer, raise error
cast floats into ints
return a + b"""
	if a != int or a != float:
		raise TypeError("a must be an integer")
	if b != int or a != float:
		raise TypeError("b must be an integer")
	else:
		a = int(a)
		b = int(b)
		return a + b
