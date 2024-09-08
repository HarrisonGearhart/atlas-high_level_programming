#!/usr/bin/python3
"""Define a class called Square with a size attribute.
Size must an integer >= 0.
property def size(self): to retrieve it
property setter def size(self, value): to set it
Raise errors if the user input is invalid
Set position property to a value
Raise an error if the value is not a tuple of 2 positive integers
use spaces for position
Returns the current area of the square
prints in stdout the square with the # characters:
if size is equal to 0, it prints an empty line"""


class Square:
	"""Square defined by its size
	property setter for size
	raises exceptions
	property setter for position
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

	@property
	def position(self):
		return (self.__position)

	@position.setter
	def position(self, value):
		if type(value) != tuple or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
		return (self.__size * self.__size)

	def my_print(self):
		if self.__size is 0:
			print("")
		for i in range(self.__position[1]):
			print("")
		for i in range(self.__size):
			print(" " * self.__position[0], end="")
			print("#" * self.__size)
