from advent_of_code.year_2015.day_16 import run

TEST_INSTRUCTIONS = [
    "Sue 1: children: 1, cars: 8, vizslas: 7",
    "Sue 2: akitas: 10, perfumes: 10, children: 5",
    "Sue 3: cars: 5, pomeranians: 4, vizslas: 1",
    "Sue 4: goldfish: 5, children: 8, perfumes: 3",
]

TARGET_SUE_COMPOUNDS_1 = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 4,
    "akitas": 0,
    "vizslas": 1,
    "goldfish": 5,
    "trees": 3,
    "cars": 5,
    "perfumes": 1,
}

TARGET_SUE_COMPOUNDS_2 = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 5,
    "akitas": 0,
    "vizslas": 1,
    "goldfish": 5,
    "trees": 3,
    "cars": 5,
    "perfumes": 1,
}


class TestPart1:
    def test_part1_example(self) -> None:
        target_sue = run.Sue(0, TARGET_SUE_COMPOUNDS_1)
        assert run.part1(TEST_INSTRUCTIONS, target_sue) == 3


class TestPart2:
    def test_part2_example(self) -> None:
        target_sue = run.Sue(0, TARGET_SUE_COMPOUNDS_2)
        assert run.part2(TEST_INSTRUCTIONS, target_sue) == 3
