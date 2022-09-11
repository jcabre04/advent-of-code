from collections import defaultdict
from itertools import combinations


def _get_valid_comb_list(
    containers: list[int], target_liters: int
) -> list[tuple[int, ...]]:
    "Return a list of combinations combinations that sum up to the target liters"
    valid = []

    for comb_length, _ in enumerate(containers, start=1):
        potential_combs = combinations(containers, comb_length)
        for potential in potential_combs:
            if sum(potential) == target_liters:
                valid.append(potential)

    return valid


def part1(containers: list[int], target_liters: int) -> int:
    "Return the number of container combinations that sum up to the target liters"
    return len(_get_valid_comb_list(containers, target_liters))


def part2(containers: list[int], target_liters: int) -> int:
    """Find the minimum number of containers that sum up to the targert liter.
    Then, return the number of combinations that sum to that minimum"""
    potentially_valid = _get_valid_comb_list(containers, target_liters)
    counter = defaultdict(list)  # keys == the len of the combinations inside its value

    for comb in potentially_valid:
        counter[len(comb)].append(comb)

    return len(counter[min(counter)])


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_17/input.txt"
    with open(input_file, "r") as file:
        instructions = [int(line.strip()) for line in file.readlines()]

    print(f"Part 1: {part1(instructions, 150)}")
    print(f"Part 2: {part2(instructions, 150)}")
