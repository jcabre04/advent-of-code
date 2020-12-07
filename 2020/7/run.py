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
	def __init__(self, name, parents=[], children=[]):
		self.name=name
		self.parents = parents # Each parent has quantity 1
		self.children = children # Each child is a tuple of (int quantity, Bag object)

	def __repr__(self):
		return "Bag '{}'".format(self.name)
		# return "Bag {} | p {} | c {}".format(self.name, self.parents, len(self.children) or 0)
		return "Bag {} {}".format(self.name, self.children)
		# return "Bag {} {}".format(self.name, self.parents)

# return a list of tuples in the form (int quantity, string child name)
def _extract_children(children):
	list_of_children = []
	for child in children:
		find_values = re.findall(r'(\d+) (\w+ \w+)', child)
		quantity, name = find_values[0]
		list_of_children.append((quantity, name))
	# print(len(list_of_children),list_of_children)
	return list_of_children

def _recursive_search(bag_dict, bag, names):
	names.append(bag_dict[bag].name)
	if bag_dict[bag].parents != []:
		for paren in bag_dict[bag].parents:
			_recursive_search(bag_dict, paren, names)

def _recursive_mul(bag_dict, bag):
	pass

@print_time_and_result
def part1(lines):
	bag_dict = {}
	for line in lines:
		if line:
			bags_parent_child = line.split(" bags contain ")
			bags_parent_child[1] = re.findall(r'(\d+ \w+ \w+) bags*', bags_parent_child[1])
			parent = str(bags_parent_child[0]).strip()
			children = _extract_children(bags_parent_child[1])

			if parent not in bag_dict:
				bag_dict[parent] = Bag(parent, children=children,parents=[])
			else:
				for child in children:
					bag_dict[parent].children.append(child)


			for child in children:
				child_name = child[1]
				if child_name not in bag_dict:
					bag_dict[child_name] = Bag(child_name, parents=[parent],children=[])
				else:
					bag_dict[child_name].parents.append(parent)

	names = []
	for paren in bag_dict['shiny gold'].parents:
		_recursive_search(bag_dict,paren, names)
	print(len(set(names)))

	return "Not started yet"

@print_time_and_result
def part2(lines):
	return "Not started yet"

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().split(".\n")

	part1(lines)
	part2(lines)
