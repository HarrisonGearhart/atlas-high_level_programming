#!/usr/bin/python3
"""This Function divides all elements of a matrix
"""

def matrix_divided(matrix, div):
	"""Divides all values by div and returns a new matrix
	matrix must be a list of floats or integers
	each row of the matrix must be the same size
	div must be a float or integer, and can't equal zero
	round to 2 decimal places"""
	if type(matrix) is not list or len(matrix) == 0:
		raise TypeError("matrix must be a list (list of lists) of integers/floats")
	if type(row) is not list for row in matrix:
		raise TypeError("matrix must be a list (list of lists) of integers/floats")
	if type(element) is not int or type(element) is not float for element in row:
		raise TypeError("matrix must be a list (list of lists) of integers/floats")
	if len(row) != len(matrix[0]) for row in matrix:
		raise TypeError("Each row of the matrix must have the same size")
	if type(div) is not int or type(div) is not float:
		raise TypeError("div must be a number")
	if div == 0:
		raise TypeError("division by zero")
	return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])