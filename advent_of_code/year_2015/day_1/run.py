def part1(input: str) -> int:
    "Tally the total assuming ( is 1 and ) is -1"
    total = 0
    for char in input:
        if char == "(":
            total += 1
        elif char == ")":
            total -= 1
    return total


def part2(input: str) -> int:
    "Find the char position that results in the first -1"
    current = 0
    for pos, char in enumerate(input, start=1):
        if char == "(":
            current += 1
        elif char == ")":
            current -= 1

        if current == -1:
            return pos
    return -1


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_1/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input[0])}")
    print(f"Part 2: {part2(input[0])}")
