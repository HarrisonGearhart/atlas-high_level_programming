#!/usr/bin/python3
def safe_print_division(a, b):
	quotient = 0
	try:
		quotient = a / b
		print("Inside result: {}".format(quotient))
	except:
		print("Inside result: {}".format(quotient))
	finally:
		return quotient
