from advent_of_code.year_2015.day_11 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert not run.is_pass_valid("hijklmmn")
        assert not run.is_pass_valid("abbceffg")
        assert not run.is_pass_valid("abbcegjk")
        assert run.is_pass_valid("abcdffaa")
        assert run.part1(["abcdefgh"]) == "abcdffaa"
        assert run.part1(["ghijklmn"]) == "ghjaabcc"


# No tests. Part2 uses the same logic as part1
# class TestPart2:
#     def test_part2_example(self) -> None:
#         # assert run.part2(")") == 1
#         pass
