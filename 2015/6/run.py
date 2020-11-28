from time import time

GRID_SIZE = 1000

def _extract_range(ranges_string):
	ranges = ranges_string.split(" through ")
	range1 = list(map(int, ranges[0].split(",")))
	range2 = list(map(int, ranges[1].split(",")))
	return range1, range2

def _change_grid_range(command, ranges, grid):
	range1, range2 = _extract_range(ranges)
	for x in range(range1[0], range2[0] + 1):
		for y in range(range1[1], range2[1] + 1):
			if command == "off":
				grid[x][y] = False
			elif command == "on":
				grid[x][y] = True
			elif command == "toggle":
				current = grid[x][y]
				if current:
					grid[x][y] = False
				else:
					grid[x][y] = True

def _process_command(command, grid):
	if "turn off" in command:
		_change_grid_range("off", command.replace("turn off ", ''), grid)
	elif "turn on" in command:
		_change_grid_range("on", command.replace("turn on ", ''), grid)
	elif "toggle" in command:
		_change_grid_range("toggle", command.replace("toggle ", ''), grid)

def _count_lights(grid):
	count = 0
	for x in range(GRID_SIZE):
		for y in range(GRID_SIZE):
			if grid[x][y]:
				count += 1
	return count


def _change_grid_range2(command, ranges, grid):
	range1, range2 = _extract_range(ranges)
	for x in range(range1[0], range2[0] + 1):
		for y in range(range1[1], range2[1] + 1):
			if command == "off":
				grid[x][y] = max(grid[x][y] - 1, 0)
			elif command == "on":
				grid[x][y] = grid[x][y] + 1
			elif command == "toggle":
				grid[x][y] = grid[x][y] + 2

def _process_command2(command, grid):
	if "turn off" in command:
		_change_grid_range2("off", command.replace("turn off ", ''), grid)
	elif "turn on" in command:
		_change_grid_range2("on", command.replace("turn on ", ''), grid)
	elif "toggle" in command:
		_change_grid_range2("toggle", command.replace("toggle ", ''), grid)

def _count_brightness(grid):
	return sum(map(sum,grid))

def part1(lines):
	grid = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
	
	for line in lines:
		_process_command(line.strip(), grid)

	return _count_lights(grid)

def part2(lines):
	grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
	
	for line in lines:
		_process_command2(line.strip(), grid)

	return _count_brightness(grid)

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.readlines()

	print("Answers below:\n")

	# start = time()
	# print("part1 answer:\t{}".format(part1(lines)))
	# print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))