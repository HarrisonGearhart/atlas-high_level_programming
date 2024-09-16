#!/usr/bin/python3
"""function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
	"""load from json file"""
	with open(filename, "r") as json_file:
		return json.load(json_file)
