from collections import defaultdict


def move(loc: list[int], dir: str) -> None:
    "Move the given location 1 unit to the given direction"
    match dir:
        case "^":
            loc[1] += 1
        case "v":
            loc[1] -= 1
        case "<":
            loc[0] -= 1
        case ">":
            loc[0] += 1


def part1(input: list[str]) -> int:
    "Count how many houses received at least one present w/ 1 deliverer"

    visited = defaultdict(lambda: 0)
    loc = [0, 0]

    visited[(loc[0], loc[1])] += 1
    for direction in input[0]:
        move(loc, direction)
        visited[(loc[0], loc[1])] += 1

    return len(visited)


def part2(input: list[str]) -> int:
    "Count how many houses received at least one present w/ 2 deliverers"

    visited = defaultdict(lambda: 0)
    santa_loc = [0, 0]
    robot_loc = [0, 0]

    visited[santa_loc[0], santa_loc[1]] += 1
    for turn, direction in enumerate(input[0]):
        if turn % 2:
            move(robot_loc, direction)
            visited[robot_loc[0], robot_loc[1]] += 1
        else:
            move(santa_loc, direction)
            visited[santa_loc[0], santa_loc[1]] += 1

    return len(visited)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_03/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
