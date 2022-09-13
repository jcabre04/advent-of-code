from advent_of_code.year_2015.day_20 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(100) == 6
        assert run.part1(150) == 8
        assert run.part1(130) == 8


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(55) == 4
        assert run.part2(101) == 6
