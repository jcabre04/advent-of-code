from time import time
import re

# Print function's answer and elapsed time taken
def print_time_and_result(function):
	def decorated(*args, **kwargs):
		start_time = time()
		result = function(*args, **kwargs)
		print("answer for {}:\t{}".format(function.__name__, result))
		print("elapsed time: {} seconds\n".format(time() - start_time))
	return decorated

class Bag():
	def __init__(self, name):
		self.name = name
		self.parents = [] # list of Bag
		self.children = [] # list of tuples form: (int quantity, Bag child)
	
	def __repr__(self):
		return "Bag {}".format(self.name)

# return a list of tuples in the form (int quantity, string child name)
def _extract_children(children):
	list_of_children = []
	for child in children:
		find_values = re.findall(r'(\d+) (\w+ \w+)', child)
		quantity, name = find_values[0]
		list_of_children.append((quantity, name))
	return list_of_children

def _recursive_part1(bag, names):
	names.add(bag.name)
	if bag.parents != []:
		for parent in bag.parents:
			_recursive_part1(parent, names)
			
def _recursive_part2(bag):
	count = 1
	if bag.children == []:
		return 1
	
	for child in bag.children:
		count += int(child[0]) * _recursive_part2(child[1])

	return count

@print_time_and_result
def _build_tree(lines):
	bags = {} # name:Bag
	for line in lines:
		parent_and_children = line.split(" bags contain ")
		parent = parent_and_children[0]
		children = _extract_children(re.findall(r'(\d+ \w+ \w+) bags*', parent_and_children[1]))

		if parent not in bags:
			bags[parent] = Bag(parent)
		
		for child in children:
			if child[1] not in bags:
				bags[child[1]] = Bag(child[1])
			bags[parent].children.append((child[0], bags[child[1]]))
			bags[child[1]].parents.append(bags[parent])
	
	outer_bags = set()
	for parent in bags['shiny gold'].parents:
		_recursive_part1(parent, outer_bags)
	print("part1 answer: {}".format(len(outer_bags)))
	
	inner_bags = 0
	for child in bags['shiny gold'].children:
		inner_bags += int(child[0]) * _recursive_part2(child[1])
	print("part2 answer: {}".format(inner_bags))
	

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().split(".\n")
		lines.remove("")

	_build_tree(lines)