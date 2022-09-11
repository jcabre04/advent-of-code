from advent_of_code.year_2015.day_01 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1("(())") == 0
        assert run.part1("()()") == 0
        assert run.part1("(((") == 3
        assert run.part1("(()(()(") == 3
        assert run.part1("())") == -1
        assert run.part1("))(") == -1
        assert run.part1(")))") == -3
        assert run.part1(")())())") == -3


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(")") == 1
        assert run.part2("()())") == 5
