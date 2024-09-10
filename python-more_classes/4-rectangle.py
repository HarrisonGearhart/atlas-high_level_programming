#!/usr/bin/python3
"""Define a class called Rectangle."""
class Rectangle:
	"""Class called Rectangle
	property set width
	property set height
	width/height must be an int >= 0
	define area and perimeter
	return rectangle in string form with #'s
	return a string representation of Rectangle
	"""
	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
	
	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value
	
	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		return (self.__width * self.__height)
	
	def perimeter(self):
		return ((self.__width * 2) + (self.__height * 2))

	def __str__(self):
		if self.__width == 0 or self.__height == 0:
			return ''
		rect_str = ''
		for y in range(self.__height):
			for x in range(self.__width):
				rect_str += '#'
			rect_str += '\n'
		return rect_str[:-1]

	def __repr__(self):
		return "Rectangle({}, {})".format(self.__width, self.__height)
		