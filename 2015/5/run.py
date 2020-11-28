from time import time

def _has_3_vowels(line):
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	for char in line:
		if char in vowels:
			count += 1

	if count >= 3:
		return True
	else:
		return False

def _has_dup_char(line):
	for index in range(len(line) - 1):
		if line[index] == line[index + 1]:
			return True

	return False

def _has_no_bad_strings(line):
	bad_strings = ['ab', 'cd', 'pq', 'xy']
	for bad in bad_strings:
		if bad in line:
			return False

	return True

def part1(lines):
	nice_strings = []
	for line in lines:
		if _has_no_bad_strings(line) and _has_3_vowels(line) and _has_dup_char(line):
			nice_strings.append(line)

	return len(nice_strings)


def _has_no_overlap_pair(line):
	while len(line) > 3:
		if line[:2] in line[2:]:
			return True
		line = line[1:]

	return False


def _has_dup_with_char_between(line):
	for index in range(len(line) - 2):
		if line[index] == line[index+2]:
			return True
	return False


def part2(lines):
	nice_strings = []
	for line in lines:
		if _has_no_overlap_pair(line) and _has_dup_with_char_between(line):
			nice_strings.append(line)

	return len(nice_strings)

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.readlines()

	print("Answers below:\n")

	start = time()
	print("part1 answer:\t{}".format(part1(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))