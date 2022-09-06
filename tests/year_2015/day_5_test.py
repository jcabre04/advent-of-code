from advent_of_code.year_2015.day_5 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(["ugknbfddgicrmopn"]) == 1
        assert run.part1(["aaa"]) == 1
        assert run.part1(["ugknbfddgicrmopn", "aaa"]) == 2
        assert run.part1(["jchzalrnumimnmhp"]) == 0
        assert run.part1(["haegwjzuvuyypxyu"]) == 0
        assert run.part1(["dvszwmarrgswjxmb"]) == 0
        assert run.part1(["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp"]) == 2


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(["qjhvhtzxzqqjkmpb"]) == 1
        assert run.part2(["xxyxx"]) == 1
        assert run.part2(["qjhvhtzxzqqjkmpb", "xxyxx"]) == 2
        assert run.part2(["uurcxstgmygtbstg"]) == 0
        assert run.part2(["ieodomkazucvgmuy"]) == 0
