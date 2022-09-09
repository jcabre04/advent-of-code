from advent_of_code.year_2015.day_13 import run


class TestPart1:
    def test_part1_example(self) -> None:
        instructions = [
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol.",
        ]
        assert run.part1(instructions) == 330
        pass


# No test. Part 2 uses the same logic as Part 1
# class TestPart2:
#     def test_part2_example(self) -> None:
#         # assert run.part2(")") == 1
#         pass
