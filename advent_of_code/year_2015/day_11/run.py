INCREMENT = {
    "a": "b",
    "b": "c",
    "c": "d",
    "d": "e",
    "e": "f",
    "f": "g",
    "g": "h",
    "h": "i",
    "i": "j",
    "j": "k",
    "k": "l",
    "l": "m",
    "m": "n",
    "n": "o",
    "o": "p",
    "p": "q",
    "q": "r",
    "r": "s",
    "s": "t",
    "t": "u",
    "u": "v",
    "v": "w",
    "w": "x",
    "x": "y",
    "y": "z",
    "z": "a",
}


def _increment_letter_at_pos(password: str, idx: int) -> str:
    "Increment the letter at the given position. Use recursion to handle wrap arounds / increasing higher 'places'"
    new_password = f"{password[:idx]}{INCREMENT[password[idx]]}{password[idx+1:]}"

    if password[idx] == "z":
        return _increment_letter_at_pos(new_password, idx - 1)

    return new_password


def _check_straight(password: str) -> bool:
    "Checks if the password contains an increasing straight"
    pos = 0
    while pos < len(password) - 2:
        chunk = password[pos : pos + 3]
        pos += 1

        # Edge case with z. Per puzzle instructions, the only valid straight with z is 'xyz'
        if "z" in chunk and "xyz" == chunk:
            return True
        elif "z" in chunk:
            continue
        # Chunk is a straight if all three chars are the same after incrementing the first twice and the second once
        elif INCREMENT[INCREMENT[chunk[0]]] == INCREMENT[chunk[1]] == chunk[2]:
            return True
        else:
            continue

    return False


def _check_bad_letter_free(password: str) -> bool:
    "Checks if the password contains bad letters"
    BAD_LETTERS = "iol"
    for letter in BAD_LETTERS:
        if letter in password:
            return False

    return True


def _check_dup_pair(password: str) -> bool:
    "Checks if the password contains two non-overlapping pairs of duplicates"

    # Loops over the entire password looking for a duplicate
    for idx1, char1 in enumerate(password[:-1]):
        if password[idx1] == password[idx1 + 1]:
            # If a dup is found, loop over the remaining part of the password looking for a dup
            for idx2, char2 in enumerate(password[idx1 + 2 : -1], start=idx1 + 2):
                if password[idx2] == password[idx2 + 1]:
                    return True
    return False


def is_pass_valid(password: str) -> bool:
    "Check if the given password is valid"
    conditions = (
        _check_straight(password),
        _check_bad_letter_free(password),
        _check_dup_pair(password),
    )
    return all(conditions)


def part1(instructions: list[str]) -> str:
    "Find a new valid password by incrementing the old once, checking, and repeating"
    password = _increment_letter_at_pos(instructions[0], len(instructions[0]) - 1)
    while not is_pass_valid(password):
        password = _increment_letter_at_pos(password, len(password) - 1)

    return password


def part2(instructions: list[str]) -> str:
    "Find the next valid password using part1's answer as the base"
    part1_answer = part1(instructions)
    return part1([part1_answer])


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_11/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
