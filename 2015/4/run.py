import hashlib
from time import time

def _find_hex_with_n_lead_zeroes(secret_key, n_zeroes):
	hexres = ''
	number = 0
	while hexres[:n_zeroes] != '0' * n_zeroes:
		print("\trequired lead 0 hash: {} | current number: {}\r".format(n_zeroes, number), end='')
		result = hashlib.md5((secret_key + str(number)).encode()) 
		hexres = result.hexdigest()
		number += 1

	print()
	return number - 1

def part1(secret_key, n_zeroes):
	return _find_hex_with_n_lead_zeroes(secret_key, n_zeroes)

def part2(secret_key, n_zeroes):
	return _find_hex_with_n_lead_zeroes(secret_key, n_zeroes)

if __name__ == '__main__':
	start = 0
	secret_key = 'ckczppom'
	print("secret_key: {}".format(secret_key))

	start = time()
	print("part1 answer:\t{}".format(part1(secret_key, 5)))
	print("elapsed time: {} seconds".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part2(secret_key, 6)))
	print("elapsed time: {} seconds".format(time() - start))