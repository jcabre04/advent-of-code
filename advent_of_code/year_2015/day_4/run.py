from hashlib import md5


def mine_until_x_prefix(prefix: str, wanted_prefix: str) -> int:
    "Turns the given prefix and real numbers into hashes until x is found"
    current = 0

    while True:
        hash = md5(f"{prefix}{str(current)}".encode())
        if wanted_prefix in str(hash.hexdigest())[: len(wanted_prefix)]:
            break
        current += 1

    return current


def part1(input: list[str]) -> int:
    "Return the lowest number to produce an MD5 hash with 5 leading zeroes"

    return mine_until_x_prefix(input[0], "00000")


def part2(input: list[str]) -> int:
    "Return the lowest number to produce an MD5 hash with 6 leading zeroes"
    return mine_until_x_prefix(input[0], "000000")


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_4/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
