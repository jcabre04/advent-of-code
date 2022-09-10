from advent_of_code.year_2015.day_15 import run


class TestPart1:
    def test_part1_example(self) -> None:
        input = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]
        assert run.part1(input) == 62842880


class TestPart2:
    def test_part2_example(self) -> None:
        input = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]
        assert run.part2(input) == 57600000
