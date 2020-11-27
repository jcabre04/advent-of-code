def part1(lines):
	coords = set()
	curx, cury = 0, 0
	coords.add((curx, cury))

	for char in lines[0]:
		if char == "^":
			cury += 1
		elif char == ">":
			curx += 1
		elif char == "v":
			cury -= 1
		elif char == "<":
			curx -= 1

		coords.add((curx, cury))

	return len(coords)

def _process_coord(char, loc):
	if char == "^":
		loc[1] += 1
	elif char == ">":
		loc[0] += 1
	elif char == "v":
		loc[1] -= 1
	elif char == "<":
		loc[0] -= 1

def part2(lines):
	santa_coords = set()
	robot_coords = set()

	santa_cur_loc = [0, 0]
	robot_cur_loc = [0, 0]

	santa_coords.add((santa_cur_loc[0], santa_cur_loc[1]))
	robot_coords.add((robot_cur_loc[0], robot_cur_loc[1]))
	
	santa_turn = True

	for char in lines[0]:
		if santa_turn:
			santa_turn = False
			_process_coord(char, santa_cur_loc)
			santa_coords.add((santa_cur_loc[0], santa_cur_loc[1]))
		else:
			santa_turn = True
			_process_coord(char, robot_cur_loc)
			robot_coords.add((robot_cur_loc[0], robot_cur_loc[1]))

	return len(santa_coords.union(robot_coords))

if __name__ == '__main__':
	input_lines = []
	with open("input.txt","r") as file:
		input_lines = [line for line in file if line]

	print("part1 answer:\t{}".format(part1(input_lines)))
	print("part2 answer:\t{}".format(part2(input_lines)))