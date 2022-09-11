from advent_of_code.year_2015.day_06 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(["turn on 0,0 through 999,999"]) == 1000000
        assert run.part1(["toggle 0,0 through 999,0"]) == 1000
        assert run.part1(["turn off 499,499 through 500,500"]) == 0
        assert run.part1(["turn on 499,499 through 500,500"]) == 4


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(["turn on 0,0 through 0,0"]) == 1
        assert run.part2(["toggle 0,0 through 999,999"]) == 2000000
        assert run.part2(["turn off 0,0 through 999,999"]) == 0

        big_input = [
            "toggle 0,0 through 999,999",
            "turn on 499,499 through 500,500",
            "turn off 0,0 through 999,999",
        ]
        assert run.part2(big_input) == 1000004
