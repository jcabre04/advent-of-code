from typing import Union
import re
from collections import defaultdict

NOT_EXPRESSION = re.compile(r"NOT (.*) -> (.*)")
AND_EXPRESSION = re.compile(r"(.*) AND (.*) -> (.*)")
OR_EXPRESSION = re.compile(r"(.*) OR (.*) -> (.*)")
LSHIFT_EXPRESSION = re.compile(r"(.*) LSHIFT (.*) -> (.*)")
RSHIFT_EXPRESSION = re.compile(r"(.*) RSHIFT (.*) -> (.*)")
ECHO_EXPRESSION = re.compile(r"(.*) -> (.*)")


def not_gate(source: list[int]) -> int:
    "Return the bitwise NOT of the first element on the list"
    binary = f"{source[0]:b}".zfill(16)
    inverse = ""

    for char in binary:
        if char == "1":
            inverse += "0"
        else:
            inverse += "1"

    return int(inverse, base=2)


def and_gate(source: list[int]) -> int:
    "Return the bitwise AND of the first two elements on the list"
    return source[0] & source[1]


def or_gate(source: list[int]) -> int:
    "Return the bitwise OR of the first two elements on the list"
    return source[0] | source[1]


def lshift_gate(source: list[int]) -> int:
    "Return the bitwise left shift of the first two elements on the list"
    return source[0] << source[1]


def rshift_gate(source: list[int]) -> int:
    "Return the bitwise right shift of the first two elements on the list"
    return source[0] >> source[1]


def echo_gate(source: list[int]) -> int:
    "Return the first element of the list"
    return source[0]


class Wire:
    def __init__(self, inputs: list = [], gate=echo_gate, signal: int = -1) -> None:
        self.inputs = inputs
        self.gate = gate
        self.signal = signal

    def calculate(self) -> int:
        "Return the signal of this Wire. Use recursion if Wire depends on other Wires"
        for idx, input in enumerate(self.inputs):
            if isinstance(input, Wire):
                self.inputs[idx] = self.inputs[idx].calculate()

        if self.signal < 0:
            self.signal = self.gate(self.inputs)

        return self.signal


def _check_exists_in_circuit(circuit, param) -> Union[int, Wire]:
    "Checks if the 'param' string is an integer value or a Wire. Convert to appropriate and return it"
    if isinstance(param, str) and not param.isdigit():
        param = circuit[param]
    else:
        param = int(param)
    return param


def assemble_circuit(instructions: list[str]) -> dict[str, Wire]:
    "Returns a dictionary representing the assembled circuit"
    circuit = defaultdict(lambda: Wire())

    for line in instructions:
        if "NOT" in line:
            data = NOT_EXPRESSION.match(line)
            assert data is not None
            source = _check_exists_in_circuit(circuit, data.group(1))
            dest = circuit[data.group(2)]
            assert isinstance(dest, Wire)
            dest.inputs = [source]
            dest.gate = not_gate
        elif "AND" in line:
            data = AND_EXPRESSION.match(line)
            assert data is not None
            source1 = _check_exists_in_circuit(circuit, data.group(1))
            source2 = _check_exists_in_circuit(circuit, data.group(2))
            dest = circuit[data.group(3)]
            assert isinstance(dest, Wire)
            dest.inputs = [source1, source2]
            dest.gate = and_gate
        elif "OR" in line:
            data = OR_EXPRESSION.match(line)
            assert data is not None
            source1 = _check_exists_in_circuit(circuit, data.group(1))
            source2 = _check_exists_in_circuit(circuit, data.group(2))
            dest = circuit[data.group(3)]
            assert isinstance(dest, Wire)
            dest.inputs = [source1, source2]
            dest.gate = or_gate
        elif "LSHIFT" in line:
            data = LSHIFT_EXPRESSION.match(line)
            assert data is not None
            source1 = _check_exists_in_circuit(circuit, data.group(1))
            source2 = _check_exists_in_circuit(circuit, data.group(2))
            dest = circuit[data.group(3)]
            assert isinstance(dest, Wire)
            dest.inputs = [source1, source2]
            dest.gate = lshift_gate
        elif "RSHIFT" in line:
            data = RSHIFT_EXPRESSION.match(line)
            assert data is not None
            source1 = _check_exists_in_circuit(circuit, data.group(1))
            source2 = _check_exists_in_circuit(circuit, data.group(2))
            dest = circuit[data.group(3)]
            assert isinstance(dest, Wire)
            dest.inputs = [source1, source2]
            dest.gate = rshift_gate
        else:
            data = ECHO_EXPRESSION.match(line)
            assert data is not None
            source = _check_exists_in_circuit(circuit, data.group(1))
            dest = circuit[data.group(2)]
            assert isinstance(dest, Wire)
            dest.inputs = [source]
            dest.gate = echo_gate

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
