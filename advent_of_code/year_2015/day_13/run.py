from re import compile, match
from collections import defaultdict
from itertools import permutations

GAIN_EXPRESSION = compile(r"(\w+) would gain (\d+) .+ to (\w+)\.")
LOSE_EXPRESSION = compile(r"(\w+) would lose (\d+) .+ to (\w+)\.")


class Person:
    "Represents a person's happiness for each potential seating partner"

    def __init__(self) -> None:
        self.connections = {}  # dict[Person,int/happiness change]


def _build_graph(instructions: list[str]) -> dict[str, Person]:
    "Build and return a graph of each Person and their happiness values"
    graph = defaultdict(lambda: Person())
    for line in instructions:
        if "gain" in line:
            data = match(GAIN_EXPRESSION, line)
            assert data is not None
            person1 = graph[data.group(1)]
            person2 = graph[data.group(3)]
            happiness = int(data.group(2))
            person1.connections[person2] = happiness
        elif "lose" in line:
            data = match(LOSE_EXPRESSION, line)
            assert data is not None
            person1 = graph[data.group(1)]
            person2 = graph[data.group(3)]
            happiness = -1 * int(data.group(2))
            person1.connections[person2] = happiness

    return graph


def _get_optimal_value(graph: dict[str, Person]) -> int:
    "Return the optimal seating (order) of all Person"
    values = set()
    for perm in permutations(graph.keys(), len(graph.keys())):
        cur_value = 0

        # Add the happiness values of all people in the middle of the permutation (list)
        for idx, name in enumerate(perm[1:-1], start=1):
            person_behind = graph[perm[idx - 1]]
            person_ahead = graph[perm[idx + 1]]
            cur_value += graph[name].connections[person_behind]
            cur_value += graph[name].connections[person_ahead]

        # Add the happiness of the people at the edges of the permutation (list)
        first_person = person_behind = graph[perm[0]]
        second_person = person_behind = graph[perm[1]]
        second_to_last = person_behind = graph[perm[-2]]
        last_person = person_behind = graph[perm[-1]]

        # First Person's happiness
        cur_value += graph[perm[0]].connections[second_person]
        cur_value += graph[perm[0]].connections[last_person]

        # Last Person's happiness
        cur_value += graph[perm[-1]].connections[first_person]
        cur_value += graph[perm[-1]].connections[second_to_last]

        values.add(cur_value)

    return max(values)


def part1(instructions: list[str]) -> int:
    "Build graph from instructions and return the value of the optimal order"
    graph = _build_graph(instructions)

    return _get_optimal_value(graph)


def part2(instructions: list[str]) -> int:
    "Adds a 'you' person to the graph with all related happines set to 0 and does the same as Part 1"
    graph = _build_graph(instructions)
    you = graph["you"]

    for person in graph.values():
        you.connections[person] = 0
        person.connections[you] = 0

    return _get_optimal_value(graph)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_13/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
