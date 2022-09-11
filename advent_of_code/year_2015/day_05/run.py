def _part1_vowel_check(string: str) -> bool:
    "Return true if 3 or more vowels exist in the string"
    VOWELS = "aeiou"
    count = 0

    for char in string:
        if char in VOWELS:
            count += 1

    return count >= 3


def _part1_dup_check(string: str) -> bool:
    "Return true if one letter appears twice in a row"
    for idx, char in enumerate(string[: len(string) - 1]):
        if char == string[idx + 1]:
            return True

    return False


def _part1_banned_string_check(string: str) -> bool:
    "Return true if no banned strings appear in the string"
    BAD_STRINGS = ["ab", "cd", "pq", "xy"]
    for bad in BAD_STRINGS:
        if bad in string:
            return False

    return True


def _part2_pair_dup_check(string: str) -> bool:
    "Return true if one pair of letters appears twice without overlapping"
    for idx in range(len(string) - 2):
        first_pair = string[idx : idx + 2]
        if first_pair in string[idx + 2 :]:
            return True

    return False


def _part2_letter_sandwich_check(string: str) -> bool:
    "Return true if a letter appears twice with a letter between them"
    for idx in range(len(string) - 2):
        if string[idx] == string[idx + 2]:
            return True

    return False


def part1(input: list[str]) -> int:
    "Counts how many strings match the given criteria"
    nice_strings = 0

    for string in input:
        conditions = (
            _part1_vowel_check(string),
            _part1_dup_check(string),
            _part1_banned_string_check(string),
        )
        if all(conditions):
            nice_strings += 1

    return nice_strings


def part2(input: list[str]) -> int:
    "Counts how many strings match the new criteria"
    nice_strings = 0

    for string in input:
        conditions = (
            _part2_pair_dup_check(string),
            _part2_letter_sandwich_check(string),
        )
        if all(conditions):
            nice_strings += 1

    return nice_strings


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_05/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
