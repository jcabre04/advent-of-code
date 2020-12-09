from time import time
from itertools import combinations as comb

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
	chunk = 25
	for index in range(chunk, len(lines)):
		previous_25_num_sums = set([nums[0] + nums[1] for nums in comb(lines[index-chunk:index], 2)])
		if lines[index] not in previous_25_num_sums:
			return "answer: ", lines[index], "index: ",index

@print_time_and_result
def part2(lines):
	index_limit = 664
	target = 1721308972
	
	for index in range(index_limit):
		count = 0
		nums_list = []
		second_pointer = index + 1

		while count < target:
			count += lines[second_pointer]
			nums_list.append(lines[second_pointer])
			if count == target:
				return max(nums_list) + min(nums_list)
			else:
				second_pointer += 1

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()
		lines = list(int(line) for line in lines)

	part1(lines)
	part2(lines)