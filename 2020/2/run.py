from time import time
import re

def _extract_info(line):
	return list(re.findall(r'(\d+)-(\d+) (\w+): (\w+)',line))[0]

def part1(lines):
	countValid = 0
	for line in lines:
		minNum, maxNum, letter, password = _extract_info(line.strip())
		if password.count(letter) >= int(minNum) and password.count(letter) <= int(maxNum):
			countValid += 1

	return countValid

def part2(lines):
	countValid = 0
	for line in lines:
		posA, posB, letter, password = _extract_info(line.strip())

		if (password[int(posA) - 1] == letter) != (password[int(posB) - 1] == letter):
			countValid += 1

	return countValid

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