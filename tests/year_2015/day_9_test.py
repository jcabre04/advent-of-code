from advent_of_code.year_2015.day_9 import run


class TestPart1:
    def test_part1_example(self) -> None:
        instructions = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]
        assert run.part1(instructions) == 605


class TestPart2:
    def test_part2_example(self) -> None:
        instructions = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]
        assert run.part2(instructions) == 982
