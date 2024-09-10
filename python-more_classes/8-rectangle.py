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
	if rectangle is deleted, prints Bye Rectangle...
	"""
	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1
	
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
				rect_str += str(self.print_symbol)
			rect_str += '\n'
		return rect_str[:-1]

	def __repr__(self):
		return "Rectangle({}, {})".format(self.__width, self.__height)
	
	def __del__(self):
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		if type(rect_1) is not Rectangle:
			raise TypeError("rect_1 must be an instance of Rectangle")
		if type(rect_2) is not Rectangle:
			raise TypeError("rect_2 must be an instance of Rectangle")
		if rect_1.area() >= rect_2.area():
			return rect_1
		return rect_2