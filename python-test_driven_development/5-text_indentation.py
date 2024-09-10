#!/usr/bin/bash
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""
def text_indentation(text):
	"""text must be a string
	adds 2 blank lines after delimeters
	no space at the beginning or at the end of each printed line
	splits the lines of text between each delimeter"
	"""
	if type(text) is not str:
		raise TypeError("text must be a string")
	for delimeter in ".:?":
		text = (delimeter + "\n\n").join([line.strip(" ") for line in text.split(delimeter)])
	print("{}".format(text), end="")