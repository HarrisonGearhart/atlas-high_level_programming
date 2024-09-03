#!/usr/bin/python3
def roman_to_int(roman_string):
	if not roman_string or type(roman_string) != str:
		return 0

	roman_dictionary = {
		"I": 1,
		"V": 5,
		"X": 10, 
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	num = 0

	for x in range(len(roman_string)):
		if roman_dictionary.get(roman_string[x], 0) == 0:
			return 0
		if (x != (len(roman_string) - 1) and roman_dictionary[roman_string[x]] < roman_dictionary[roman_string[x + 1]]):
			num += roman_dictionary[roman_string[x]] * -1
		else:
			num += roman_dictionary[roman_string[x]]
	return (num)