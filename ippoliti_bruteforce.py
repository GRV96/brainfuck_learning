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


def generate_bruteforce_nums(start, end, length):
	if length < 1 or end < start:
		return None

	delta = end - start

	if delta < length:
		return None

	size = delta ** length
	numbers = [[0 for _ in range(length)] for _ in range(size)]

	for j in range(length-1, -1, -1):
		column_param = length - j

		for i in range(0, size-(delta*column_param)+1, delta ** column_param):
			row_index = i

			for n in range(start, end):

				for _ in range(delta ** (column_param-1)):
					numbers[row_index][j] = n
					row_index += 1

	return numbers


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
			numbers.append([int(n) for n in num_strs])

	return numbers


def write_bruteforce_numbers(num_path, numbers):
	
	with num_path.open(mode=MODE_W) as num_file:

		for nums in numbers:
			num_file.write(STR_SPACE.join(nums) + STR_NEW_LINE)


bruteforce_num_path = Path("./ippoliti_bruteforce_nums.txt").resolve()
input_path = Path("./ippoliti_input.txt").resolve()

if bruteforce_num_path.exists():
	numbers = read_bruteforce_numbers(bruteforce_num_path)
else:
	numbers = generate_bruteforce_nums(0, 128, 8)
	write_bruteforce_numbers(bruteforce_num_path, numbers)

for nums in numbers:
	input_chars = make_tmp_input_file(input_path, nums)

	with redirect_stdout(StringIO()) as beef_output:
		system(f"beef -i {input_path} ippoliti.bf")
		result = beef_output.getvalue()

		if result == STR_EXCLAIM:
			print(nums)
			print(input_chars)

input_path.unlink()

