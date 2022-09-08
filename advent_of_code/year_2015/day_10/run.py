def simulate_game(start_string: str, rounds: int) -> int:
    "Simulate the game for the given amount of rounds. Then, return the output's length"
    while rounds:
        new_string = []
        cur_char = start_string[0]
        cur_count = 1

        for char in start_string[1:]:
            if char == cur_char:
                cur_count += 1
            else:
                new_string.append(str(cur_count))
                new_string.append(cur_char)
                cur_char = char
                cur_count = 1

        new_string.append(str(cur_count))
        new_string.append(cur_char)

        start_string = "".join(new_string)

        rounds -= 1

    return len(start_string)


def part1(instructions: list[str]) -> int:
    "Simulate the game for 40 rounds with the puzzle's input"
    return simulate_game(instructions[0], 40)


def part2(instructions: list[str]) -> int:
    "Simulate the game for 50 rounds with the puzzle's input"
    return simulate_game(instructions[0], 50)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_10/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
