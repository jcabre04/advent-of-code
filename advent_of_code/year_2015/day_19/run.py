class Replacement:
    "Represents a single element sequence replacement"

    def __init__(self, start_seq: str, end_seq: str) -> None:
        self.start_seq = start_seq
        self.end_seq = end_seq

    def __repr__(self) -> str:
        return f"{self.start_seq}:{self.end_seq}"


def _create_repl_list(instructions: list[str]) -> list[Replacement]:
    "Return a list of Replacements based on the puzzle's instructions"
    replacements = []
    for line in instructions:
        start_seq, end_seq = line.split(" => ")
        replacements.append(Replacement(start_seq, end_seq))

    return replacements


def part1(instructions: list[str], start: str) -> int:
    "Return the number of unique molecules (strings) after one replcement"
    molecules = set()
    replacements = _create_repl_list(instructions)

    for rep in replacements:
        rep_len = len(rep.start_seq)

        for idx in range(len(start) - (rep_len - 1)):
            cur_chunk = start[idx : idx + rep_len]

            if cur_chunk == rep.start_seq:
                molecules.add(start[:idx] + rep.end_seq + start[idx + rep_len :])

    return len(molecules)


def _reduce(
    replacements: list[Replacement], cur_count: int, cur_str: str, target: str
) -> int:
    "Using recursion, find the how many steps it takes to go from cur_str to target"
    global FOUND
    if FOUND or ("e" in cur_str and len(cur_str) > 1):
        return 0

    if cur_str == target:
        FOUND = True
        return cur_count

    molecules = set()

    # Get all molecules possible after reducing them once
    for rep in replacements:
        rep_len = len(rep.end_seq)

        for idx in range(len(cur_str) - (rep_len - 1)):
            cur_chunk = cur_str[idx : idx + rep_len]

            if cur_chunk == rep.end_seq:
                molecules.add(cur_str[:idx] + rep.start_seq + cur_str[idx + rep_len :])

    if len(molecules) < 1:
        return 0

    answer = 2**20  # Impossibly large number of steps to make first comparison work
    for mol in molecules:
        new_answer = _reduce(replacements, cur_count + 1, mol, target)
        if new_answer != 0:
            answer = min(new_answer, answer)

    return answer


def part2(instructions: list[str], start: str) -> int:
    "Returns the minimum number of steps needed to reach the target medicine (str) from 'e'"
    global FOUND
    FOUND = False

    return _reduce(_create_repl_list(instructions), 0, start, "e")


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_19/input.txt"
    with open(input_file, "r") as file:
        replacements = []
        start = ""
        for line in file.readlines():
            if "=>" in line:
                replacements.append(line.strip())
            else:
                start = line.strip()

    print(f"Part 1: {part1(replacements, start)}")
    print(f"Part 2: {part2(replacements, start)}")
