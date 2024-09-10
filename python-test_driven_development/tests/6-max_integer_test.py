#!/usr/bin/python3
#6-max_integer_test.py
"""Unit test for max integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	def test_max(self):
		self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
		self.assertAlmostEqual(max_integer([25, 50, 100, 75]), 100)
		self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
		self.assertAlmostEqual(max_integer([]), None)

	def test_non_int(self):
		self.assertRaises(TypeError, max_integer, True)
