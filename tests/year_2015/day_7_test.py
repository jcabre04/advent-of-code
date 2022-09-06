from advent_of_code.year_2015.day_7 import run


class TestPart1:
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
        assert circuit["x"].signal == 123
        assert circuit["y"].signal == 456
        circuit["d"].calculate()
        circuit["e"].calculate()
        circuit["f"].calculate()
        circuit["g"].calculate()
        circuit["h"].calculate()
        assert circuit["i"].calculate() == 65079
        assert circuit["d"].signal == 72
        assert circuit["e"].signal == 507
        assert circuit["f"].signal == 492
        assert circuit["g"].signal == 114
        assert circuit["h"].signal == 65412
        assert circuit["i"].signal == 65079

    def test_not_instruction(self) -> None:
        input = ["NOT 10 -> a", "NOT c -> b", "NOT a -> c"]
        circuit = run.assemble_circuit(input)
        assert circuit["a"].calculate() == 65525
        assert circuit["c"].calculate() == 10
        assert circuit["b"].calculate() == 65525


class TestPart2:
    def test_part2_example(self) -> None:
        # assert run.part2(")") == 1
        pass
