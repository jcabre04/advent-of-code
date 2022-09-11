from advent_of_code.year_2015.day_08 import run


class TestPart1:
    def test_part1_example(self) -> None:
        instructions = [
            '""',
            '"abc"',
            '"aaa\\"aaa"',
            '"\\x27"',
        ]
        assert run.part1(instructions) == 12


class TestPart2:
    def test_part2_example(self) -> None:
        instructions = [
            '""',
            '"abc"',
            '"aaa\\"aaa"',
            '"\\x27"',
        ]
        assert run.part2(instructions) == 19
