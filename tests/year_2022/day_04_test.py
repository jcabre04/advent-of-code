from advent_of_code.year_2022.day_04 import run

TEST_INPUT = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_INPUT) == 2


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_INPUT) == 4
