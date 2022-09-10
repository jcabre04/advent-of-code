from advent_of_code.year_2015.day_14 import run


class TestPart1:
    def test_part1_example(self) -> None:
        instructions = [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ]
        assert run.part1(instructions, 1000) == 1120


class TestPart2:
    def test_part2_example(self) -> None:
        instructions = [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ]
        assert run.part2(instructions, 1000) == 689
