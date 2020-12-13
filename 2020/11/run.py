from time import time
import hashlib 
import copy

# Print function's answer and elapsed time taken
def print_time_and_result(function):
	def decorated(*args, **kwargs):
		start_time = time()
		result = function(*args, **kwargs)
		print("answer for {}:\t{}".format(function.__name__, result))
		print("elapsed time: {} seconds\n".format(time() - start_time))
		return result
	return decorated

def _hash(matrix):
	result = hashlib.md5(str(matrix).encode()).digest()
	return (result)

def _return_adjacent_occupied(matrix, row, col):
	occupied = 0
	MAX_ROW = len(matrix)
	MAX_COL = len(matrix[0])

	UpL = matrix[row-1][col-1] if row-1 >= 0 and col-1 >= 0 else "."
	UpM = matrix[row-1][col] if row-1 >= 0 else "."
	UpR = matrix[row-1][col+1] if row-1 >= 0 and col+1 < MAX_COL else "."

	MiL = matrix[row][col-1] if col-1 >= 0 else "."
	MiR = matrix[row][col+1] if col+1 < MAX_COL else "."

	LoL = matrix[row+1][col-1] if row+1 < MAX_ROW and col-1 >= 0 else "."
	LoM = matrix[row+1][col] if row+1 < MAX_ROW else "."
	LoR = matrix[row+1][col+1] if row+1 < MAX_ROW and col+1 < MAX_COL else "."
	
	return [UpL, UpM, UpR, MiL, MiR, LoL, LoM, LoR].count("#")


def _simulate_once(old, new):
	MAX_ROW = len(matrix)
	MAX_COL = len(matrix[0])

	for index_row, row in enumerate(old):
		for index_col, seat in enumerate(row):
			if seat == "L" and _return_adjacent_occupied(old, index_row, index_col) == 0:
				new[index_row][index_col] = "#"
			elif seat == "#" and _return_adjacent_occupied(old, index_row, index_col) >= 4:
				new[index_row][index_col] = "L"


def _return_count(matrix):
	count = 0
	for row in matrix:
		for seat in row:
			if seat == "#":
				count += 1
	return count

@print_time_and_result
def part1(matrix):
	new_matrix = copy.deepcopy(matrix)
	_simulate_once(matrix, new_matrix)

	while _hash(new_matrix) != _hash(matrix):
		matrix = copy.deepcopy(new_matrix)
		_simulate_once(matrix, new_matrix)

	return _return_count(new_matrix)

def _return_occupied_part2(matrix, row, col):
	occupied = 0
	MAX_ROW = len(matrix)
	MAX_COL = len(matrix[0])

	def _find_seat_loop(matrix, row, rowInc, col, colInc):
		seat = "."
		row += rowInc
		col += colInc

		while seat == "." and row >= 0 and row < MAX_ROW and col >= 0 and col < MAX_COL:
			seat = matrix[row][col]
			row += rowInc
			col += colInc
		return seat

	UpL = _find_seat_loop(matrix, row, -1, col, -1)
	UpM = _find_seat_loop(matrix, row, -1, col, 0)
	UpR = _find_seat_loop(matrix, row, -1, col, 1)

	MiL = _find_seat_loop(matrix, row, 0, col, -1)
	MiR = _find_seat_loop(matrix, row, 0, col, 1)

	LoL = _find_seat_loop(matrix, row, 1, col, -1)
	LoM = _find_seat_loop(matrix, row, 1, col, 0)
	LoR = _find_seat_loop(matrix, row, 1, col, 1)
	
	return [UpL, UpM, UpR, MiL, MiR, LoL, LoM, LoR].count("#")

def _simulate_once_part2(old, new):
	MAX_ROW = len(matrix)
	MAX_COL = len(matrix[0])

	for index_row, row in enumerate(old):
		for index_col, seat in enumerate(row):
			if seat == "L" and _return_occupied_part2(old, index_row, index_col) == 0:
				new[index_row][index_col] = "#"
			elif seat == "#" and _return_occupied_part2(old, index_row, index_col) >= 5:
				new[index_row][index_col] = "L"

@print_time_and_result
def part2(matrix):
	new_matrix = copy.deepcopy(matrix)
	_simulate_once(matrix, new_matrix)

	while _hash(new_matrix) != _hash(matrix):
		matrix = copy.deepcopy(new_matrix)
		_simulate_once_part2(matrix, new_matrix)

	return _return_count(new_matrix)

if __name__ == '__main__':
	with open("input.txt","r") as file:
		matrix = [[seat for seat in lines] for lines in file.read().splitlines()]

	matrix_backup = copy.deepcopy(matrix)

	part1(matrix)
	part2(matrix_backup)