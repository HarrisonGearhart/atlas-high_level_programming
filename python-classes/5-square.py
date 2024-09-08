#!/usr/bin/python3
"""Define a class called Square with a size attribute.
Size must an integer >= 0.
property def size(self): to retrieve it
property setter def size(self, value): to set it
Raise errors if the user input is invalid
Returns the current area of the square
prints in stdout the square with the # characters:
if size is equal to 0, it prints an empty line"""


class Square:
	"""Square defined by its size
	property setter for size
	raises exceptions
	returns the current area
	prints the square with #s, or empty line if size is 0"""
	def __init__(self, size=0):
		self.__size = size

	@property
	def size(self):
		return self.__size
	
	@size.setter
	def size(self, size):
		if type(size) != int:
			raise TypeError("size must be an integer")
		if size < 0:
			raise TypeError("size must be >= 0")
		self.__size = size

	def area(self):
		return (self.__size * self.__size)

	def my_print(self):
		if self.__size is 0:
			print("")
		for i in range(self.__size):
			print("#" * self.__size)
