def part1():
	with open("input.txt", "r") as file:
		parens = file.readline().strip()
		return parens.count("(") - parens.count(")")

def part2():
	with open("input.txt", "r") as file:
		parens = file.readline().strip()
		currentFloor = 0
		for char, index in zip(parens, range(len(parens))):
			if char == "(":
				currentFloor += 1
			else:
				currentFloor -= 1
			if currentFloor < 0:
				return index + 1
	return 0

if __name__ == '__main__':
	print("Part1 answer: {}".format(part1()))
	print("Part2 answer: {}".format(part2()))
