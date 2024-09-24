#!/usr/bin/python3
"""Define a Sqaure Class that inherits from Rectangle model"""
from models.rectangle import Rectangle


class Square(Rectangle):
	"""Sqaure class inheriting from Rectangle"""
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)
		self.__size = size

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		self.size = value
		self.width = value
		self.height = value
