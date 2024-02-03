#!/usr/bin/python3

from contextlib import redirect_stdout
from io import StringIO
from os import system
from pathlib import Path


MODE_R = "r"
MODE_W = "w"

STR_EMPTY = ""
STR_EXCLAIM = "!"
STR_NEW_LINE = "\n"
STR_SPACE = " "


def generate_bruteforce_nums(lower_bound, upper_bound, length):
	if length < 1:
		raise ValueError("The length must be greater than or equal to 1.")

	if upper_bound < lower_bound:
		upper_bound, lower_bound = lower_bound, upper_bound

	delta = upper_bound - lower_bound

	if length > delta:
		raise ValueError(
			"The length must not exceed the gap between the bounds.")

	d = delta + 1
	for i in range(d ** length):
		numbers = [i % d + lower_bound]

		for j in range(length-2, -1, -1):
			n = (i // (d ** (length - j - 1))) % d + lower_bound
			numbers.insert(0, n)

		yield numbers


def make_tmp_input_file(input_path, input_nums):

	with input_path.open(mode=MODE_W) as input_file:
		input_chars = STR_EMPTY.join(chr(n) for n in input_nums)
		input_file.write(input_chars)

	return input_chars


def read_bruteforce_numbers(num_path):
	numbers = list()

	with num_path.open(mode=MODE_R) as num_file:
		text = num_file.read()
		lines = text.split(STR_NEW_LINE)

		for line in lines:
			num_strs = line.split(STR_SPACE)

			try:
				numbers = [int(n) for n in num_strs]
			except ValueError:
				continue

			yield numbers


def write_bruteforce_numbers(num_path, numbers):
	
	with num_path.open(mode=MODE_W) as num_file:

		for nums in numbers:
			nums_as_str = [str(n) for n in nums]
			num_file.write(STR_SPACE.join(nums_as_str) + STR_NEW_LINE)


input_path = Path("./ippoliti_input.txt").resolve()
beef_cmd = f"beef -i {input_path} ippoliti.bf"
numbers = generate_bruteforce_nums(0, 128, 8)

for nums in numbers:
	input_chars = make_tmp_input_file(input_path, nums)

	with redirect_stdout(StringIO()) as beef_output:
		system(beef_cmd)
		result = beef_output.getvalue()

		if result == STR_EXCLAIM:
			print(nums)
			print(input_chars)

input_path.unlink()

