from time import time

def _process_1_seat(seat, return_row_col=False):
	rows = [num for num in range(128)]
	cols = [num for num in range(8)]

	seat_row = seat[:7]
	seat_col = seat[7:]

	for char in seat_row:
		if char == 'F':
			rows = rows[:len(rows)//2]
		else:
			rows = rows[len(rows)//2:]

	for char in seat_col:
		if char == 'L':
			cols = cols[:len(cols)//2]
		else:
			cols = cols[len(cols)//2:]

	if return_row_col:
		return rows[0], cols[0]
	else:
		return rows[0] * 8 + cols[0]

def part1(lines):
	return max(_process_1_seat(seat) for seat in lines)

def part2(lines):
	seats = [["_" for _ in range(8)] for _ in range(128)]
	for seat in lines:
		row, col = _process_1_seat(seat, return_row_col=True)
		seats[row][col] = "X"

	for seat_row in range(128):
		print("{}\t".format(seat_row),end='')
		for seat_col in range(8):
			print("{}({})\t".format(seats[seat_row][seat_col], seat_row*8+seat_col),end='')
		print()

	return ("Search for lone \'_\' in the output above. Answer in ()")

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	print("Answers below:\n")

	start = time()
	print("part1 answer:\t{}".format(part1(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))