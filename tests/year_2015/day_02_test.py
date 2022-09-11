from advent_of_code.year_2015.day_02 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(["2x3x4"]) == 58
        assert run.part1(["1x1x10"]) == 43
        assert run.part1(["2x3x4", "1x1x10"]) == 101


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(["2x3x4"]) == 34
        assert run.part2(["1x1x10"]) == 14
        assert run.part2(["2x3x4", "1x1x10"]) == 48
