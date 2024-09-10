#!/usr/bin/python3
"""This function test the max integer in a given list"""

def max_integer(list=[]):
	"""Function finds and returns max int
	if the list is empty return None
	"""
	if len(list) == 0:
		return None
	max = list[0]
	n = 1
	while n < len(list):
		if list[n] > max:
			max = list[n]
		n += 1
	return max
