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

@print_time_and_result
def part1(lines):
	differences = [0 for _ in range(len(lines) - 1)]
	for index in range(1, len(lines)):
		differences[index-1] = lines[index] - lines[index-1]

	return differences.count(1) * differences.count(3)

@print_time_and_result
def part2(lines):
	paths = differences = [0 for _ in range(len(lines) - 1)]
	paths[0] = 1
	for index in range(len(lines)-2):
		paths[index + 1] += paths[index]
		if index + 2 < len(lines)-1 and lines[index+2] - lines[index] <= 3:
			paths[index+2] += paths[index]
		if index + 3 < len(lines)-1 and lines[index+3] - lines[index] <= 3:
			paths[index+3] += paths[index]
	return paths[-1]

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = [int(line) for line in file.read().splitlines()]

	lines.append(0)					# Outlet
	lines.append(max(lines) + 3)	# Device
	lines.sort()

	iteration = 0
	part1(lines)
	part2(lines)