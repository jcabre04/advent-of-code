# For part 1, used GeeksforGeeks' algorithm to find all divisors of a natural number:
# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
import math


def part1(target: int) -> int:
    "Returns the lowest house number of the house that gets at least as many presents as the puzzle input"

    cur_house = 1
    # Count the presents of each house, one at a time, until target presents are reached
    # Presents are equal to the sum of house numbers divisors * 10
    while True:
        presents = 0
        cur_elf = 1

        while cur_elf <= math.sqrt(cur_house):
            if cur_house % cur_elf == 0:
                if cur_house / cur_elf == cur_elf:
                    presents += cur_elf * 10
                else:
                    presents += cur_elf * 10 + cur_house // cur_elf * 10
            cur_elf += 1

        if presents >= target:
            break

        cur_house += 1

    return cur_house


def part2(target: int) -> int:
    "Using the updated rules for elves, return the minimum house number that gets at least as many presents as target"

    # Calculate the presents received by the houses.
    houses = [0 for x in range(target)]
    for elf in range(1, len(houses) // 11 + 1):
        present_limit = 50
        for house in range(elf, len(houses), elf):
            houses[house] += 11 * elf
            present_limit -= 1
            if present_limit == 0:
                break

    # Find the lowest house number with presents <= target
    answer = 0
    for house_idx, presents in enumerate(houses):
        if presents >= target:
            answer = house_idx
            break

    return answer


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_20/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(int(instructions[0]))}")
    print(f"Part 2: {part2(int(instructions[0]))}")
