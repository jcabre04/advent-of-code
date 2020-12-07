import sys
import pathlib

TEMPLATE_RUN_PY = '''from time import time

# Print function's answer and elapsed time taken
def print_time_and_result(function):
	def decorated(*args, **kwargs):
		start_time = time()
		result = function(*args, **kwargs)
		print("answer for {}:\\t{}".format(function.__name__, result))
		print("elapsed time: {} seconds\\n".format(time() - start_time))
	return decorated

@print_time_and_result
def part1(lines):
	return "Not started yet"

@print_time_and_result
def part2(lines):
	return "Not started yet"

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	part1(lines)
	part2(lines)
'''

def create_files(target_path):
	# Empty instructions.txt
	(target_path / "instructions.txt").write_text("")

	# Empty input.txt
	(target_path / "input.txt").write_text("")

	# Template of run.py
	(target_path / "run.py").write_text(TEMPLATE_RUN_PY)
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please specify a folder within this one")
		sys.exit()

	current_path = pathlib.Path(".")
	target_path = current_path / '//'.join([arg for arg in sys.argv[1:]])

	if target_path.is_dir():
		# print target_path is directory == True
		print("{} is a directory".format(target_path.resolve()))

	else: # Create a directory at the specifed path 
		target_path.mkdir(parents=True)

	# Create default files
	create_files(target_path)