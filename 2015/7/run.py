from time import time
import operator

class Gate():
	def __init__(self, val1=None, val2=None, operation=None, output=None):
		self.val1=val1
		self.val2=val2
		self.operation=operation
		self.output=output

	def return_output(self, wires):
		if self.output != None:
			if isinstance(self.output, int):
				return self.output
			else:
				self.output = wires[self.output].return_output(wires)
				return self.output
		else:
			v1, v2 = None, None
			if isinstance(self.val1, int):
				v1 = self.val1
			else:
				v1 = wires[self.val1].return_output(wires)

			if isinstance(self.val2, int):
				v2 = self.val2
			else:
				v2 = wires[self.val2].return_output(wires)
			self.output = self.operation(v1, v2)
			return self.output

	def __repr__(self):
		return "val1: {}|\tval2: {}\t|oper: {}|\toutput: {}".format(self.val1, self.val2, self.operation, self.output)

def _return_digit_else_string(val):
	if val.isdigit():
		return int(val)
	else:
		return val

def _extract_values(line):
	target, val1, val2, operation, output = None, None, None, None, None
	split1 = line.split(" -> ")
	target = _return_digit_else_string(split1[1])
	if "AND" in line:
		values = split1[0].split(" AND ")
		val1 = _return_digit_else_string(values[0])
		val2 = _return_digit_else_string(values[1])
		operation = operator.and_
	elif "OR" in line:
		values = split1[0].split(" OR ")
		val1 = _return_digit_else_string(values[0])
		val2 = _return_digit_else_string(values[1])
		operation = operator.or_
	elif "LSHIFT" in line:
		values = split1[0].split(" LSHIFT ")
		val1 = _return_digit_else_string(values[0])
		val2 = _return_digit_else_string(values[1])
		operation = operator.lshift
	elif "RSHIFT" in line:
		values = split1[0].split(" RSHIFT ")
		val1 = _return_digit_else_string(values[0])
		val2 = _return_digit_else_string(values[1])
		operation = operator.rshift
	elif "NOT" in line: # 65535 MINUS <<>>
		values = split1[0].split("NOT ")
		val1 = 65535
		val2 = _return_digit_else_string(values[1])
		operation = operator.sub
	else: #assign
		output = _return_digit_else_string(split1[0])
	return target, val1, val2, operation, output

def _set_up(line, wires):
	target, val1, val2, operation, output = _extract_values(line.strip())
	if output != None:
		wires[target] = Gate(output=output)
	else:
		wires[target] = Gate(val1=val1, val2=val2, operation=operation)

def part1(lines):
	wires = {}
	for line in lines:
		_set_up(line.strip(), wires)

	return wires['a'].return_output(wires)

def part2(lines):
	return "Same as part1 but 1 line of input is changed"

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