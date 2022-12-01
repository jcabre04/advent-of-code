def part1(elves: list[int]) -> int:
    "Return the highest amount of calories carried by one elf"
    return max(elves)


def part2(elves: list[int]) -> int:
    "Return the total calories carried by the top three elves"
    return sum(sorted(elves, reverse=True)[:3])


if __name__ == "__main__":
    input_file = "advent_of_code/year_2022/day_1/input.txt"
    with open(input_file, "r") as file:
        current_elf = 0
        elves = []

        for line in file.readlines():
            line = line.strip()
            if line.isnumeric():
                current_elf += int(line)
            else:
                elves.append(current_elf)
                current_elf = 0

        elves.append(current_elf)

    print(f"Part 1: {part1(elves)}")
    print(f"Part 2: {part2(elves)}")
