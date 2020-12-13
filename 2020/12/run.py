from time import time

# Print function's answer and elapsed time taken
def print_time_and_result(function):
	def decorated(*args, **kwargs):
		start_time = time()
		result = function(*args, **kwargs)
		print("answer for {}:\t{}".format(function.__name__, result))
		print("elapsed time: {} seconds\n".format(time() - start_time))
		return result
	return decorated

def _compas_move(location, instruction, amount):
	amount = int(amount)
	if instruction == "N":
		location[1] += amount
	elif instruction == "E":
		location[0] += amount
	elif instruction == "S":
		location[1] -= amount
	elif instruction == "W":
		location[0] -= amount

def _direction_change(direction, instruction, amount):
	dir_number = {"N":0, "E":90, "S":180, "W":270, 0:"N",90:"E",180:"S",270:"W"}
	current_dir = dir_number[direction]
	amount = int(amount)
	while amount:
		if instruction == "L":
			current_dir -= 90
		elif instruction == "R":
			current_dir += 90
		amount -= 90

	return dir_number[current_dir % 360]

@print_time_and_result
def part1(lines):
	location = [0, 0] # Origin
	direction = "E" # Start facing East
	direction_vals = {"N":[0, 1], "E":[1, 0], "S":[0, -1], "W":[-1, 0]}

	for line in lines:
		instruction = line[0]
		if instruction in ["N","E","S","W"]:
			_compas_move(location, instruction, line.replace(instruction, ""))
		elif instruction in ["L","R"]:
			direction = _direction_change(direction, instruction, line.replace(instruction, ""))
		elif instruction in ["F"]:
			vals = direction_vals[direction]
			location[0] += (int(line[1:]) * vals[0])
			location[1] += (int(line[1:]) * vals[1])

	return abs(location[0]) + abs(location[1])

def _direction_change_L(direction, amount):
	amount = int(amount)
	x = direction[0]
	y = direction[1]
	while amount:
		temp_x = x
		temp_y = y
		if x == 0 or y == 0:
			if x == 0 and y == 0:
				pass
			elif x == 0 and y > 0:
				x =  y * -1
				y = 0
			elif y == 0 and x < 0:
				y = x
				x = 0
			elif x == 0 and y < 0:
				x = y * -1
				y = 0
			elif x > 0 and y == 0:
				y = x
				x = 0
		else:
			if x > 0 and y >= 0:
				y = temp_x
				x = temp_y * -1
			elif x < 0 and y > 0:
				x = temp_y * -1
				y = temp_x
			elif x < 0 and y < 0:
				y = temp_x
				x = temp_y * -1
			elif x > 0 and y < 0:
				x = temp_y * -1
				y = temp_x
		amount -= 90

	return [x, y]

def _direction_change_R(direction, amount):
	amount = int(amount)
	x = direction[0]
	y = direction[1]
	while amount:
		temp_x = x
		temp_y = y
		if x == 0 or y == 0:
			if x == 0 and y == 0:
				pass
			elif x == 0 and y > 0:
				x = y
				y = 0
			elif y == 0 and x < 0:
				y = x * -1
				x = 0
			elif x == 0 and y < 0:
				x = y
				y = 0
			elif x > 0 and y == 0:
				y = x * -1
				x = 0
		else:
			if x > 0 and y > 0:
				x = temp_y
				y = temp_x * -1
			elif x < 0 and y > 0:
				x = temp_y
				y = temp_x * -1
			elif x < 0 and y < 0:
				x = temp_y
				y = temp_x * -1
			elif x > 0 and y < 0:
				x = temp_y
				y = temp_x * -1
		amount -= 90

	return [x, y]

@print_time_and_result
def part2(lines):
	boat_location = [0, 0] # Origin
	wayp_location = [10, 1] # Waypoint relative to ship
	auto = ""

	for line in lines:
		instruction = line[0]
		if instruction in ["N","E","S","W"]:
			_compas_move(wayp_location, instruction, line.replace(instruction, ""))
		elif instruction in ["L"]:
			wayp_location = _direction_change_L(wayp_location, line.replace(instruction, ""))
		elif instruction in ["R"]:
			wayp_location = _direction_change_R(wayp_location, line.replace(instruction, ""))
		elif instruction in ["F"]:
			boat_location[0] += (int(line[1:]) * wayp_location[0])
			boat_location[1] += (int(line[1:]) * wayp_location[1])

	return abs(boat_location[0]) + abs(boat_location[1])

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	part1(lines)
	part2(lines)