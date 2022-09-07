import re
from typing import Union
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


def _check_exists_in_circuit(
    circuit: defaultdict[str, Wire], param: str
) -> Union[int, Wire]:
    "Checks if the 'param' string is an integer value or a Wire. Convert to appropriate and return it"
    if isinstance(param, str) and not param.isdigit():
        converted = circuit[param]
    else:
        converted = int(param)
    return converted


def _process_instr_1_param(
    circuit: defaultdict[str, Wire], line: str, re_expression: re.Pattern[str], function
) -> None:
    "Process NOT and ECHO instructions, setting up the wire for this instruction"
    data = re_expression.match(line)
    assert data is not None
    source = _check_exists_in_circuit(circuit, data.group(1))
    dest = circuit[data.group(2)]
    assert isinstance(dest, Wire)
    dest.inputs = [source]
    dest.gate = function


def _process_instr_2_param(
    circuit: defaultdict[str, Wire], line: str, re_expression: re.Pattern[str], function
) -> None:
    "Process AND, OR, LSHIFT, and RSHIFT instructions, setting up the wire for this instruction"
    data = re_expression.match(line)
    assert data is not None
    source1 = _check_exists_in_circuit(circuit, data.group(1))
    source2 = _check_exists_in_circuit(circuit, data.group(2))
    dest = circuit[data.group(3)]
    assert isinstance(dest, Wire)
    dest.inputs = [source1, source2]
    dest.gate = function


def assemble_circuit(instructions: list[str]) -> dict[str, Wire]:
    "Returns a dictionary representing the assembled circuit"
    circuit = defaultdict(lambda: Wire())

    for line in instructions:
        if "NOT" in line:
            _process_instr_1_param(circuit, line, NOT_EXPRESSION, not_gate)
        elif "AND" in line:
            _process_instr_2_param(circuit, line, AND_EXPRESSION, and_gate)
        elif "OR" in line:
            _process_instr_2_param(circuit, line, OR_EXPRESSION, or_gate)
        elif "LSHIFT" in line:
            _process_instr_2_param(circuit, line, LSHIFT_EXPRESSION, lshift_gate)
        elif "RSHIFT" in line:
            _process_instr_2_param(circuit, line, RSHIFT_EXPRESSION, rshift_gate)
        else:
            _process_instr_1_param(circuit, line, ECHO_EXPRESSION, echo_gate)

    return circuit


def part1(input: list[str]) -> int:
    "Assemble a circuit with the given instructions and find the signal of Wire 'a'"
    circuit = assemble_circuit(input)
    return circuit["a"].calculate()


def part2(input: list[str]) -> int:
    "Overwrite Wire's b initial signal with the answer for part1. Then, redo part1 to find the new Wire 'a' signal"
    part1_answer = part1(input)
    input[input.index("1674 -> b")] = f"{part1_answer} -> b"
    return part1(input)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_7/input.txt"
    with open(input_file, "r") as file:
        input = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
