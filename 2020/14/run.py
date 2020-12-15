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
	mask = ""
	memory = {}
	for line in lines:
		if "mask" in line:
			mask = line.replace("mask = ","")
		else:
			mem_slot, mem_value = line.replace("mem[","").split("] = ")
			new_val = ""
			for val_bit, mask_bit in zip(bin(int(mem_value)).replace("0b","").zfill(36), mask):
				if mask_bit == "X":
					new_val += val_bit
				else:
					new_val += mask_bit
			memory[mem_slot] = int(new_val,2)

	return sum(memory.values())

def _add_val_to_mems(memory, mem_value, new_slot):
	if "X" in new_slot:
		_add_val_to_mems(memory, mem_value, new_slot.replace("X", "1", 1))
		_add_val_to_mems(memory, mem_value, new_slot.replace("X", "0", 1))
	else:
		memory[new_slot] = int(mem_value)

@print_time_and_result
def part2(lines):
	mask = ""
	memory = {}
	for line in lines:
		if "mask" in line:
			mask = line.replace("mask = ","")
		else:
			mem_slot, mem_value = line.replace("mem[","").split("] = ")
			new_slot = ""
			for slot_bit, mask_bit in zip(bin(int(mem_slot)).replace("0b","").zfill(36), mask):
				if mask_bit == "0":
					new_slot += slot_bit
				elif mask_bit == "1":
					new_slot += "1"
				elif mask_bit == "X":
					new_slot += "X"

			_add_val_to_mems(memory, int(mem_value), new_slot)

	return sum(memory.values())

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	part1(lines)
	part2(lines)