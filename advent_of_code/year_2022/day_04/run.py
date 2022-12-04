from typing import Set


def range_to_set(bounds: str) -> Set[int]:
    low, high = map(int, bounds.split("-"))
    return {num for num in range(low, high + 1)}


def part1(pairs: list[str]) -> int:
    "Return the number of pairs with one range fully containing the other"
    count = 0

    for pair in pairs:
        pair_1, pair_2 = pair.split(",")
        set_1 = range_to_set(pair_1)
        set_2 = range_to_set(pair_2)

        if set_1.issubset(set_2) or set_2.issubset(set_1):
            count += 1

    return count


def part2(pairs: list[str]) -> int:
    "Return the number of pairs that overlap at all"
    count = 0

    for pair in pairs:
        pair_1, pair_2 = pair.split(",")
        set_1 = range_to_set(pair_1)
        set_2 = range_to_set(pair_2)

        if set_1.intersection(set_2) != set():  # set() is the empty set
            count += 1

    return count


if __name__ == "__main__":
    input_file = "advent_of_code/year_2022/day_04/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
