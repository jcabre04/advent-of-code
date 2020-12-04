from time import time
import re

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
OPTIONAL_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

def _buid_passport(vals):
	passport = {}
	
	for line in vals:
		pairs = line.split()
		for pair in pairs:
			key_val = pair.split(":")
			passport[key_val[0]] = key_val[1]
	
	return passport

def _is_valid_fields(set_of_fields):
	return set_of_fields == REQUIRED_FIELDS or set_of_fields == OPTIONAL_FIELDS

def _fields_pass_validation(passport):
	byr, iyr, eyr, hgt = passport['byr'], passport['iyr'], passport['eyr'], passport['hgt']
	hcl, ecl, pid = passport['hcl'], passport['ecl'], passport['pid']
 
	if not (len(byr) == 4 and byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002):
		return False

	if not (len(iyr) == 4 and iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020):
		return False

	if not (len(eyr) == 4 and eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030):
		return False
		
	if "cm" in hgt:
		hgt = hgt.replace("cm","")
		if not (hgt.isdigit() and int(hgt) >= 150 and int(hgt) <= 193):
			return False
	elif "in" in hgt:
		hgt = hgt.replace("in","")
		if not (hgt.isdigit() and int(hgt) >= 59 and int(hgt) <= 76):
			return False
	else:
		return False

	if "#" in hcl and len(hcl) == 7:
		hcl = hcl.replace("#","")
		for char in hcl:
			if not (char in "0123456789abcdef"):
				return False
	else:
		return False

	if not (ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
		return False

	if not (pid.isdigit() and len(pid) == 9):
		return False
	
	return True
	
def _valid_passport_count(passports, ignore_field_validation=True):
	valid = 0
	for passport in passports:
		fields = set(passport.keys())
		if _is_valid_fields(fields) and ignore_field_validation:
			valid += 1
		elif _is_valid_fields(fields) and _fields_pass_validation(passport):
			valid += 1

	return valid

def part1(lines, part1=True):
	lines.append("")
	passport_vals = []
	passports = []
	for line in lines:
		if line:
			passport_vals.append(line)
		else:
			passports.append(_buid_passport(passport_vals))
			passport_vals = []

	if part1:
		return _valid_passport_count(passports)
	else:
		return _valid_passport_count(passports, ignore_field_validation=False)

def part2(lines):
	pass # part2 taken care of by part1()

if __name__ == '__main__':
	with open("input.txt","r") as file:
		lines = file.read().splitlines()

	print("Answers below:\n")

	start = time()
	print("part1 answer:\t{}".format(part1(lines)))
	print("elapsed time: {} seconds\n".format(time() - start))

	start = time()
	print("part2 answer:\t{}".format(part1(lines, part1=False)))
	print("elapsed time: {} seconds\n".format(time() - start))