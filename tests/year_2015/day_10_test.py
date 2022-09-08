from advent_of_code.year_2015.day_10 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.simulate_game("1", 5) == 6
        assert run.simulate_game("11", 4) == 6
        assert run.simulate_game("21", 3) == 6
        assert run.simulate_game("1211", 2) == 6
        assert run.simulate_game("111221", 1) == 6


# No tests for part2. It uses the same logic as part1
# class TestPart2:
#     def test_part2_example(self) -> None:
#         # assert run.part2(")") == 1
#         pass
