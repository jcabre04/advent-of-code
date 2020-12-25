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

def _insert_into_mem(memory, key, value):
	if key in memory:
		memory[key].pop(0)
		memory[key].append(value)
	else:
		memory[key] = [None, value]

def _play(target):
	memory = {12: [None,1], 1:[None,2], 16:[None,3], 3:[None,4], 11:[None,5], 0:[None,6]}
	last_spoken = 0
	current_turn = 7

	while current_turn <= target:
		if memory[last_spoken][0] == None:
			_insert_into_mem(memory, 0, current_turn)
			last_spoken = 0
		else:
			last_spoken = memory[last_spoken][1] - memory[last_spoken][0]
			_insert_into_mem(memory, last_spoken, current_turn)

		current_turn += 1

	return last_spoken

@print_time_and_result
def part1(target):
	return _play(target)

@print_time_and_result
def part2(target):
	return _play(target)

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	part1(2020)
	part2(30000000)