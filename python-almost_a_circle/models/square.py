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
		return self.__width

	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		"""update args"""
		if args and len(args) != 0:
			a = 0
			for arg in args:
				if a == 0:
					if arg is None:
						self.__init__(self.size, self.x, self.y)
					else:
						self.id = arg
				elif a == 1:
					self.size = arg
				elif a == 2:
					self.x = arg
				elif a == 3:
					self.y = arg
				a += 1
		elif kwargs and len(kwargs) != 0:
			for key, value, in kwargs.items():
				if key == "id":
					if value is None:
						self.__init__(self.size, self.x, self.y)
					else:
						self.id = value
				elif key == "size":
					self.size = value
				elif key == "x":
					self.x = value
				elif key == "y":
					self.y = value
