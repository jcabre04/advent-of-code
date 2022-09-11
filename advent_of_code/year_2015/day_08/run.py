def _count_decoded_chars(line: str) -> int:
    "Return the number of characters in memory that the line would produce"
    line = line[1:-1]  # Remove the quotes encapsulating the string

    total = 0
    idx = 0
    while idx < len(line):
        match line[idx : idx + 2]:
            case r"\\" | r"\"":
                idx += 2
            case r"\x":
                idx += 4
            case _:
                idx += 1
        total += 1

    return total


def _count_encoded_chars(line: str) -> int:
    "Return the number of characters in memory that the line would produce"
    line = line[1:-1]  # Remove the quotes encapsulating the string

    total = 6  # From the quotes encapsulating the string
    idx = 0
    while idx < len(line):
        match line[idx : idx + 2]:
            case r"\\" | r"\"":
                idx += 2
                total += 4
            case r"\x":
                idx += 4
                total += 5
            case _:
                idx += 1
                total += 1

    return total


def part1(instructions: list[str]) -> int:
    "Return the total number of characters in the string minus the number of characers in memory"
    string_chars, memory_chars = 0, 0
    for line in instructions:
        string_chars += len(line)
        memory_chars += _count_decoded_chars(line)

    return string_chars - memory_chars


def part2(instructions: list[str]) -> int:
    "Return the total number of encoded characters minus the number of characters in the string"
    string_chars, encoded_chars = 0, 0
    for line in instructions:
        string_chars += len(line)
        encoded_chars += _count_encoded_chars(line)

    return encoded_chars - string_chars


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_08/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
