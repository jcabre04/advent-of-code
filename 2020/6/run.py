from time import time

QUESTION_LABELS = 'abcdefghijklmnopqrstuvwxyz'

def _translte_1_person(answers):
	return [1 if QUESTION_LABELS[index] in answers else 0 for index in range(26)]

def _compare_group_answers_AND(answers):
	mask = int('1' * 26, base=2)

	for answer in answers:
		mask = mask & int(''.join(map(str,answer)),base=2)

	return bin(mask).count('1')

def _compare_group_answers_OR(answers):
	mask = int('0' * 26, base=2)

	for answer in answers:
		mask = mask | int(''.join(map(str,answer)),base=2)

	return bin(mask).count('1')

def _get_summed_groups_answer(all_groups, compare_method):
	all_group_answers = []

	current_group = []
	for group in all_groups:
		if group != '':
			current_group.append(_translte_1_person(group))
		elif current_group != []:
			all_group_answers.append(compare_method(current_group))
			current_group = []

	return sum(all_group_answers)

def part1(lines):
	return _get_summed_groups_answer(lines, _compare_group_answers_OR)

def part2(lines):
	return _get_summed_groups_answer(lines, _compare_group_answers_AND)

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()
		lines.append("")

	print("Answers below:\n")

	start = time()
	print("part1 answer:\t{}".format(part1(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))