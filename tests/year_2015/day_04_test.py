from advent_of_code.year_2015.day_04 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(["abcdef"]) == 609043
        assert run.part1(["pqrstuv"]) == 1048970


# No tests. This part uses the same logic as part 1
# class TestPart2:
#     def test_part2_example(self) -> None:
#         pass
