#!/usr/bin/python3
"""This Function divides all elements of a matrix
"""

def matrix_divided(matrix, div):
	"""Divides all values by div and returns a new matrix
	matrix must be a list of floats or integers
	each row of the matrix must be the same size
	div must be a float or integer, and can't equal zero
	round to 2 decimal places"""
	if type(matrix) is not list:
		raise TypeError("matrix must be a list (list of lists) of integers/floats")
	size = None
	for x in matrix:
		if type(nums) is not list:
			raise TypeError("matrix must be a matrix (list of lists) of integers")
		if size is None:
			size = len(x)
		elif size != len(x):
			raise TypeError("Each row of the matrix must have the same size")
		for y in x:
			if type(y) is not int and type(y) is not float:
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		if type(div) is not int and type(div) is not float:
			raise TypeError("div must be a number")
		if div == 0:
			raise ZeroDivisionError("division by zero")
		return [[round(y / div, 2) for y in x] for x in matrix]
		