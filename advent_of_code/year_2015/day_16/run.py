from re import compile, match

DATA_EXPRESSION = compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")


class Sue:
    "Represents one Aunt Sue"

    def __init__(self, name: int, known_compounds: dict[str, int]) -> None:
        self.name = name
        self.compounds = known_compounds


def _get_sues(instructions: list[str]) -> list[Sue]:
    "Using the instructions, extract the known compounds for each Sue and return a list of them"
    sues = []
    for line in instructions:
        data = match(DATA_EXPRESSION, line)
        assert data is not None
        name, comp1, val1, comp2, val2, comp3, val3 = data.groups()
        known_compounds = {comp1: int(val1), comp2: int(val2), comp3: int(val3)}
        sues.append(Sue(int(name), known_compounds))

    return sues


def part1(instructions: list[str], target_sue: Sue) -> int:
    "Return the Sue's number that matches the target_sue's known compounds"
    sues = _get_sues(instructions)

    for potential_sue in sues:

        # Each Sue from the instructions only has 3 known compounds. All must match to be the right Sue
        matches = 0
        for potential_comp, potential_val in potential_sue.compounds.items():
            if potential_val == target_sue.compounds[potential_comp]:
                matches += 1

        if matches == 3:
            return potential_sue.name

    return 0  # A zero means no Sue was found


def part2(instructions: list[str], target_sue: Sue) -> int:
    "Return the Sue's number that matches the target_sue's known compounds using new matching instructions"
    sues = _get_sues(instructions)

    for potential_sue in sues:

        # Each Sue from the instructions only has 3 known compounds. All must match to be the right Sue
        matches = 0
        for potential_comp, potential_val in potential_sue.compounds.items():

            match potential_comp:
                case "cats" | "trees":
                    if potential_val > target_sue.compounds[potential_comp]:
                        matches += 1
                case "pomeranians" | "goldfish":
                    if potential_val < target_sue.compounds[potential_comp]:
                        matches += 1
                case _:
                    if potential_val == target_sue.compounds[potential_comp]:
                        matches += 1

        if matches == 3:
            return potential_sue.name

    return 0  # A zero means no Sue was found


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_16/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    # These numbers are from the puzzle's instructions
    target_sue_compounds = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    target_sue = Sue(0, target_sue_compounds)

    print(f"Part 1: {part1(instructions, target_sue)}")
    print(f"Part 2: {part2(instructions, target_sue)}")
