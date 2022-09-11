from advent_of_code.year_2015.day_07 import run


class TestPart1:
    def test_echo_instruction(self) -> None:
        input = ["10 -> a", "a -> b"]
        circuit = run.assemble_circuit(input)
        assert circuit["a"].calculate() == 10
        assert circuit["b"].calculate() == 10

    def test_not_instruction(self) -> None:
        input = ["NOT 10 -> a", "NOT c -> b", "NOT a -> c"]
        circuit = run.assemble_circuit(input)
        assert circuit["a"].calculate() == 65525
        assert circuit["c"].calculate() == 10
        assert circuit["b"].calculate() == 65525

    def test_and_instruction(self) -> None:
        input = ["3 -> a", "9 -> b", "a AND b -> c", "4 AND 12 -> d"]
        circuit = run.assemble_circuit(input)
        assert circuit["c"].calculate() == 1
        assert circuit["d"].calculate() == 4

    def test_or_instruction(self) -> None:
        input = ["3 -> a", "9 -> b", "a OR b -> c", "4 OR 3 -> d"]
        circuit = run.assemble_circuit(input)
        assert circuit["c"].calculate() == 11
        assert circuit["d"].calculate() == 7

    def test_lshift_instruction(self) -> None:
        input = ["4 -> a", "a LSHIFT 2 -> b", "1 LSHIFT 3 -> c"]
        circuit = run.assemble_circuit(input)
        assert circuit["b"].calculate() == 16
        assert circuit["c"].calculate() == 8

    def test_rshift_instruction(self) -> None:
        input = ["16 -> a", "a RSHIFT 2 -> b", "8 RSHIFT 3 -> c"]
        circuit = run.assemble_circuit(input)
        assert circuit["b"].calculate() == 4
        assert circuit["c"].calculate() == 1

    def test_part1_example(self) -> None:
        input = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
        circuit = run.assemble_circuit(input)
        assert circuit["x"].calculate() == 123
        assert circuit["y"].calculate() == 456
        assert circuit["i"].calculate() == 65079
        assert circuit["d"].calculate() == 72
        assert circuit["e"].calculate() == 507
        assert circuit["f"].calculate() == 492
        assert circuit["g"].calculate() == 114
        assert circuit["h"].calculate() == 65412
        assert circuit["i"].calculate() == 65079


# None for part2 since it uses all the same logic as part1
# class TestPart2:
#     def test_part2_example(self) -> None:
#         # assert run.part2(")") == 1
#         pass
