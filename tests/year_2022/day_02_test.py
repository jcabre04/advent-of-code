from advent_of_code.year_2022.day_02 import run

TEST_INPUT = ["A Y", "B X", "C Z"]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_INPUT) == 15


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_INPUT) == 12
