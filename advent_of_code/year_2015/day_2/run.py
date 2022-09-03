def part1(input: list[str]) -> int:
    "Return total wrapping paper needed for all presents"
    total = 0
    for present in input:
        dimensions = [int(dim) for dim in present.split("x")]
        lxw = dimensions[0] * dimensions[1]
        wxh = dimensions[1] * dimensions[2]
        hxl = dimensions[2] * dimensions[0]

        total += 2 * lxw + 2 * wxh + 2 * hxl + min(lxw, wxh, hxl)

    return total


def part2(input: list[str]) -> int:
    "Return total ribbon needed for all presents"
    total = 0
    for present in input:
        dimensions = [int(dim) for dim in present.split("x")]
        volume = dimensions[0] * dimensions[1] * dimensions[2]
        shortest = min(dimensions)
        dimensions.remove(shortest)
        short = min(dimensions)

        total += 2 * shortest + 2 * short + volume

    return total


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_2/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
