import numpy as np
import re

# Compiled re expression are faster than interpreted ones against large number of uses.
EXPRESSION = re.compile(r".* (\d+,\d+) through (\d+,\d+)")


def _get_start_n_end(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    "Extract and return the start and end points from the string instruction"
    result = EXPRESSION.match(line)
    assert result is not None
    s = tuple(map(int, result.group(1).split(",")))
    e = tuple(map(int, result.group(2).split(",")))
    return s, e


def _change_grid(grid: np.ndarray, line: str, TURN_ON, TURN_OFF, TOGGLE) -> None:
    "Change the grid using the given (lambda) functions. Generalized to accomdate different sets of instructions"
    s, e = _get_start_n_end(line)
    for col in range(s[0], e[0] + 1):
        for row in range(s[1], e[1] + 1):
            if "turn on" in line:
                grid[col][row] = TURN_ON(grid[col][row])
            elif "turn off" in line:
                grid[col][row] = TURN_OFF(grid[col][row])
            elif "toggle" in line:
                grid[col][row] = TOGGLE(grid[col][row])


def part1(input: list[str]) -> int:
    "Find how many lights are on after perfoming the given instructions"
    grid = np.zeros((1000, 1000), dtype=np.short)

    for line in input:
        _change_grid(
            grid,
            line,
            lambda _: 1,  # TURN_ON
            lambda _: 0,  # TURN_OFF
            lambda num: 1 - num,  # TOGGLE
        )

    return grid.sum()


def part2(input: list[str]) -> int:
    "Find the intensity of the lights after perfoming the new instructions"
    grid = np.zeros((1000, 1000), dtype=np.short)

    for line in input:
        _change_grid(
            grid,
            line,
            lambda num: num + 1,  # TURN_ON
            lambda num: max(num - 1, 0),  # TURN_OFF
            lambda num: num + 2,  # TOGGLE
        )

    return grid.sum()


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_06/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
