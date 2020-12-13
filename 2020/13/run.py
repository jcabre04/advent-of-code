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
	time_zero = int(lines[0])
	current_time = time_zero
	bus_ids = [int(bus) for bus in lines[1].split(",") if bus != "x"]

	print(current_time)
	while True:
		for bus in bus_ids:
			if current_time % bus == 0:
				return bus * (current_time - time_zero)
		current_time += 1

@print_time_and_result
def part2(lines):
	current_time = 0
	bus_ids = []
	offsets = []
	offset_from_last_bus = 0

	for bus in lines[1].split(","):
		if bus != "x":
			offsets.append(offset_from_last_bus)
			bus_ids.append(int(bus))
		offset_from_last_bus += 1


	departure_ids = [
	    (int(v), (int(v) - i) % int(v))
	    for i, v in enumerate(lines[1].split(","))
	    if v != "x"
	]

	i = 0
	k = departure_ids[i][0]
	increment = k
	while True:
	    div, mod = departure_ids[i + 1]
	    if k % div == mod:
	        if i == len(departure_ids) - 2:
	            print(k)
	            break
	        increment *= div
	        i += 1
	    k += increment

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	# part1(lines)
	part2(lines)
