def find_priority_score(letter: str) -> int:
    subtrahend = 0
    if letter in ("abcdefghijklmnopqrstuvwxyz"):
        subtrahend = 96
    elif letter in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        subtrahend = 38

    return ord(letter) - subtrahend


def part1(bags: list[str]) -> int:
    "Find the item type that appears in both compartments of each rucksack. Return the sum of their priorities"
    score = 0
    for bag in bags:
        half_a = set(bag[: len(bag) // 2])
        half_b = set(bag[len(bag) // 2 :])
        priority = half_a.intersection(half_b)
        score += find_priority_score(list(priority)[0])

    return score


def part2(bags: list[str]) -> int:
    "Find the item type that corresponds to the badges of each three-Elf group. Return the sum of their priorities"
    score = 0
    for index in range(0, len(bags), 3):
        bag_1 = set(bags[index + 0])
        bag_2 = set(bags[index + 1])
        bag_3 = set(bags[index + 2])
        priority = bag_1.intersection(bag_2).intersection(bag_3)
        score += find_priority_score(list(priority)[0])

    return score


if __name__ == "__main__":
    input_file = "advent_of_code/year_2022/day_03/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
