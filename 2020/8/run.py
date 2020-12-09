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

#@print_time_and_result
def part1(lines):
	current_instruction = 0
	accumulator = 0
	times_ran = [0 for _ in range(len(lines))]
	
	while current_instruction < len(lines):
		inst = lines[current_instruction]
		times_ran[current_instruction] += 1

		if times_ran[current_instruction] > 1:
			return False, accumulator		
		
		if 'nop' in inst:
			pass
		elif 'acc' in inst:
			accumulator += int(lines[current_instruction].replace("acc ", ""))
		elif 'jmp' in inst:
			current_instruction += int(lines[current_instruction].replace("jmp ", ""))
			continue
		
		current_instruction += 1

	return True, accumulator

#@print_time_and_result
def part2(lines):
	backup = lines.copy()
	current_instruction = 0
	accumulator = 0
	times_ran = [0 for _ in range(len(lines))]
	order_ran = [0 for _ in range(len(lines))]
	order_count = 1
	
	while current_instruction < len(lines):
		inst = lines[current_instruction]
		times_ran[current_instruction] += 1
		order_ran[current_instruction] = order_count
		
		if times_ran[current_instruction] > 1:
			fixed_lines = False
			
			while not fixed_lines:
				new_lines = backup.copy()
				if "jmp" in new_lines[order_ran.index(order_count)]:
					new_lines[order_ran.index(order_count)] = new_lines[order_ran.index(order_count)].replace("jmp", "nop")
				elif "nop" in new_lines[order_ran.index(order_count)]:
					new_lines[order_ran.index(order_count)] = new_lines[order_ran.index(order_count)].replace("nop", "jmp")
				
				fixed_lines, new_accumulator = part1(new_lines)
				if fixed_lines:
					return new_accumulator
				
				order_count -= 1
		
		order_count += 1

		if 'nop' in inst:
			pass
		elif 'acc' in inst:
			accumulator += int(lines[current_instruction].replace("acc ", ""))
		elif 'jmp' in inst:
			current_instruction += int(lines[current_instruction].replace("jmp ", ""))
			continue
		
		current_instruction += 1

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	print("Part1 answer: ",part1(lines)[1])
	print("Part2 answer: ",part2(lines))