from time import time

def _slope_checker(lines, rightStep, downStep):
	width = len(lines[0])
	height = len(lines)
	treeHits = 0
	right = 0
	down = 0
	
	while down < height:
		if lines[down][right] == "#":
			treeHits += 1
		
		right += rightStep
		down += downStep
		
		if right >= width:
			right -= width
		
	return treeHits

def part1(lines):
	return _slope_checker(lines=lines, rightStep=3, downStep=1)

def part2(lines):
	r1d1 = _slope_checker(lines=lines, rightStep=1, downStep=1)
	r3d1 = _slope_checker(lines=lines, rightStep=3, downStep=1)
	r5d1 = _slope_checker(lines=lines, rightStep=5, downStep=1)
	r7d1 = _slope_checker(lines=lines, rightStep=7, downStep=1)
	r1d2 = _slope_checker(lines=lines, rightStep=1, downStep=2)
	
	return r1d1 * r3d1 * r5d1 * r7d1 * r1d2

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	print("Answers below:\n")

	start = time()
	print("part1 answer:\t{}".format(part1(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))