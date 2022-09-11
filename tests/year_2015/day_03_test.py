from advent_of_code.year_2015.day_03 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1([">"]) == 2
        assert run.part1(["^>v<"]) == 4
        assert run.part1(["^v^v^v^v^v"]) == 2


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(["^v"]) == 3
        assert run.part2(["^>v<"]) == 3
        assert run.part2(["^v^v^v^v^v"]) == 11
