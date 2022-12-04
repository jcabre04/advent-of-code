def part1(encryption: list[str]) -> int:
    "Return the score represented by the encrypted input. Assume the second column is a shape like the first."
    choice_score = {"X": 1, "Y": 2, "Z": 3}
    match_score = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    score = 0

    for pair in encryption:
        them, mine = pair.split()
        score += choice_score[mine]
        score += match_score[them][mine]

    return score


def part2(encryption: list[str]) -> int:
    "Return the score represented by the encrypted input. The second indicates the required outcome."
    choice_score = {"rock": 1, "paper": 2, "scissors": 3}
    match_score = {"X": 0, "Y": 3, "Z": 6}
    find_choice = {
        "A": {"X": "scissors", "Y": "rock", "Z": "paper"},
        "B": {"X": "rock", "Y": "paper", "Z": "scissors"},
        "C": {"X": "paper", "Y": "scissors", "Z": "rock"},
    }

    score = 0

    for pair in encryption:
        them, outcome = pair.split()
        score += match_score[outcome]
        score += choice_score[find_choice[them][outcome]]

    return score


if __name__ == "__main__":
    input_file = "advent_of_code/year_2022/day_2/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
