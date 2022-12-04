from advent_of_code.year_2022.day_01 import run

TEST_INPUT = [6000, 4000, 11000, 24000, 10000]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_INPUT) == 24000


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_INPUT) == 45000
