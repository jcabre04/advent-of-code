import re
import json
from typing import Union


def _json_walkthrough(json_struct: Union[list, dict, str, int]) -> int:
    "Iterates over a json structure, ignores objects/dicts with 'red', adds all integers, and returns the total"
    total = 0
    if isinstance(json_struct, int):
        return json_struct
    elif isinstance(json_struct, list):
        for item in json_struct:
            total += _json_walkthrough(item)
    elif isinstance(json_struct, dict):
        if "red" not in json_struct.keys() and "red" not in json_struct.values():
            for key, val in json_struct.items():
                total += _json_walkthrough(key)
                total += _json_walkthrough(val)

    return total


def part1(instructions: list[str]) -> int:
    "Return the sum of all numbers found within the json string"
    num_iterable = map(int, re.findall(r"-?\d+", instructions[0]))

    return sum(num_iterable)


def part2(instructions: list[str]) -> int:
    "Return the sum of all numbers found within the json string that are not part of a red object/dict"
    json_struct = json.loads(instructions[0])

    return _json_walkthrough(json_struct)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_12/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
