from advent_of_code.year_2015.day_19 import run

TEST_PUZZLE_REPLACEMENTS_PART1 = [
    "H => HO",
    "H => OH",
    "O => HH",
]

TEST_PUZZLE_REPLACEMENTS_PART2 = [
    "e => H",
    "e => O",
    "H => HO",
    "H => OH",
    "O => HH",
]


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1(TEST_PUZZLE_REPLACEMENTS_PART1, "HOH") == 4
        assert run.part1(TEST_PUZZLE_REPLACEMENTS_PART1, "HOHOHO") == 7


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2(TEST_PUZZLE_REPLACEMENTS_PART2, "HOH") == 3
        assert run.part2(TEST_PUZZLE_REPLACEMENTS_PART2, "HOHOHO") == 6
        assert run.part2(TEST_PUZZLE_REPLACEMENTS_PART2, "HHHHHHHHH") == 9
