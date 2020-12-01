from time import time

def part1(lines):
	lines = list(map(int,lines))
	
	while lines:
		currentNum = lines.pop()
		for number in lines:
			if currentNum + number == 2020:
				return currentNum * number

	return "Failed!"

def part2(lines):
	lines = list(map(int,lines))
	
	while lines:
		firstNum = lines.pop()
		midList = lines.copy()
		while midList:
			secondNum = midList.pop()
			for thirdNumber in midList:
				if firstNum + secondNum + thirdNumber == 2020:
					return firstNum * secondNum * thirdNumber

	return "Failed!"

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