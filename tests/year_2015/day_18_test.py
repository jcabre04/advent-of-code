from advent_of_code.year_2015.day_18 import run

TEST_INSTRUCTIONS_PART1 = [
    ".#.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####..",
]

TEST_INSTRUCTIONS_PART2 = [
    "##.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####.#",
]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_INSTRUCTIONS_PART1, 6, 4) == 4


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_INSTRUCTIONS_PART1, 6, 5) == 17
