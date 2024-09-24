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
		self.width = self.height = value

	def update(self, *args, **kwargs):
		"""update args"""
		attr = ["id", "size", "x", "y"]
		if args:
			for att, num in zip(attr, args):
				setattr(self, att, num)
		elif kwargs:
			for key, value in kwargs.items():
				if key in attr:
					setattr(self, key, value)
