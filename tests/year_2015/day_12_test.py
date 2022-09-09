from advent_of_code.year_2015.day_12 import run


class TestPart1:
    def test_part1_example(self) -> None:
        assert run.part1([r"[1,2,3]"]) == 6
        assert run.part1([r'{"a":2,"b":4}']) == 6
        assert run.part1([r"[[[3]]]"]) == 3
        assert run.part1([r'{"a":{"b":4},"c":-1}']) == 3
        assert run.part1([r'{"a":[-1,1]}']) == 0
        assert run.part1([r'[-1,{"a":1}]']) == 0
        assert run.part1([r"{}"]) == 0
        assert run.part1([r"[]"]) == 0


class TestPart2:
    def test_part2_example(self) -> None:
        assert run.part2([r'["red",1,2,3]']) == 6
        assert run.part2([r'[1,{"c":"red","b":2},3]']) == 4
        assert run.part2([r'{"d":"red","e":[1,2,3,4],"f":5}']) == 0
        assert run.part2([r'[1,"red",5]']) == 6
