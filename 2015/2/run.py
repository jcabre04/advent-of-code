def part1():
	total_wrap_paper = 0
	with open("input.txt","r") as file:
		for line in file:
			x, y, z = map(int, line.split("x"))
			xy = x*y 
			yz = y*z
			zx = z*x
			total_wrap_paper += 2*xy + 2*yz + 2*zx + min(xy,yz,zx)
	return total_wrap_paper

def part2():
	total_wrap_ribbon = 0
	with open("input.txt","r") as file:
		for line in file:
			dim = list(map(int, line.split("x")))
			dim.sort()
			total_wrap_ribbon += dim[0] + dim[0] + dim[1] + dim[1]

			total_wrap_ribbon += dim[0] * dim[1] * dim[2]

	return total_wrap_ribbon

if __name__ == '__main__':
	print(part1())
	print(part2())