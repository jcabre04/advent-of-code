RUN_DEFAULT = """def part1(instructions: list[str]) -> int:
    "Part 1"
    return 0


def part2(instructions: list[str]) -> int:
    "Part 2"
    return 0


if __name__ == "__main__":
    input_file = "advent_of_code/{}/{}/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {{part1(instructions)}}")
    print(f"Part 2: {{part2(instructions)}}")
"""

INPUT_DEFAULT = """"""

TEST_DEFAULT = """from advent_of_code.{}.{} import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1([]) == 0


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2([]) == 0
"""
