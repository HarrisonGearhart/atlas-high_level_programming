#!/usr/bin/python3
"""Rectangle Class that inherets from Base Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    width and height attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
