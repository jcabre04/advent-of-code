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

	# print(sum(lines))

	# print("diff 1: {}\tdiff 2: {}\t diff 3:{}".format(differences.count(1), differences.count(2),differences.count(3)))
	return differences.count(1) * differences.count(3)

#@print_time_and_result
def part2(lines,iteration):
	valid = 0
	while len(lines) > 2:
		if len(lines) > 3 and lines[3] - lines[0] == 3: # Can remove 2
			valid += 2
			# print(lines[:1] + lines[1+1:])
			# print(lines[:1] + lines[2+1:])
			valid += part2(lines[:1] + lines[1+1:], iteration+1)
			valid += part2(lines[:1] + lines[2+1:], iteration+1)

		elif lines[2] - lines[0] <= 2: # Can remove 1
			valid += 1
			# print(lines[:1] + lines[1:])
			valid += part2(lines[:1] + lines[1+1:],iteration+1)

		del lines[0]

	print("\t",valid," ","*"*iteration*2,iteration)
	return valid

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = [int(line) for line in file.read().splitlines()]

	lines.append(0)					# Outlet
	lines.append(max(lines) + 3)	# Device
	lines.sort()

	iteration = 0
	part1(lines)
	print(part2(lines,iteration))

# Mini_input
# diff 1: 7       diff 2: 0        diff 3:5
# d1 * d3 = 35
# Arrangements = 8
# input size = 13

# Mini_input2
# diff 1: 22      diff 2: 0        diff 3:10
# d1 * d3 = 220
# Arrangements = 19208
# input size = 33

# input
# diff 1: 72      diff 2: 0        diff 3:33
# d1 * d3 = 2376
# Arrangments = ??
# input size = 106