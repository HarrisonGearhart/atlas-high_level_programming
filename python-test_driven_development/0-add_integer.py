#!/usr/bin/python3
"""This function adds two integers"""

def add_integer(a, b=98):
	if a != int or a != float:
		raise TypeError("a must be an integer")
	if b != int or a != float:
		raise TypeError("b must be an integer")
	else:
		return a + b
