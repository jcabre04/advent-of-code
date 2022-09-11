from advent_of_code.year_2015.day_17 import run

TEST_INSTRUCTIONS = [20, 15, 10, 5, 5]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_INSTRUCTIONS, 25) == 4


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_INSTRUCTIONS, 25) == 3
