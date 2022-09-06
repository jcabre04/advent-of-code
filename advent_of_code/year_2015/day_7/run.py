import re
from collections import defaultdict


NOT_EXPRESSION = re.compile(r"NOT (.*) -> (.*)")


def echo_gate(source: list[int]) -> int:
    return source[0]


def not_gate(source: list[int]) -> int:
    print(source)
    binary = f"{source[0]:b}".zfill(16)
    inverse = ""

    for char in binary:
        if char == "1":
            inverse += "0"
        else:
            inverse += "1"

    return int(inverse, base=2)


class Wire:
    def __init__(self, inputs: list = [], gate=echo_gate, signal: int = -1) -> None:
        self.inputs = inputs
        self.gate = gate
        self.signal = signal

    def calculate(self) -> int:
        for idx, input in enumerate(self.inputs):
            if isinstance(input, Wire):
                self.inputs[idx] = self.inputs[idx].calculate()

        if self.signal < 0:
            self.signal = self.gate(self.inputs)

        return self.signal


def assemble_circuit(lines: list[str]) -> dict[str, Wire]:
    circuit = defaultdict(lambda: Wire())

    for line in lines:
        if "NOT" in line:
            data = NOT_EXPRESSION.match(line)
            assert data is not None
            source = data.group(1)
            if isinstance(source, str) and not source.isdigit():
                source = circuit[source]
            else:
                source = int(source)
            dest = data.group(2)
            dest = circuit[dest]
            dest.inputs = [source]
            dest.gate = not_gate

    return circuit


def part1(input: list[str]) -> int:
    "Part 1"
    return 0


def part2(input: list[str]) -> int:
    "Part 2"
    return 0


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_7/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
