import re
from collections import defaultdict
from itertools import permutations

DATA_EXPRESSION = re.compile(r"(\w*) to (\w*) = (\d*)")


class Node:
    "Representation of a graph node. In this simple problem, only needs connection and weight to other nodes"

    def __init__(self) -> None:
        self.connections = {}  # dict[Node, int] or dict[city, distance]


def _build_graph(instructions: list[str]) -> dict[str, Node]:
    "Create and return the graph as described by the instructions"
    graph = defaultdict(lambda: Node())  # dict[str, Node] or dict[city name, city]

    for line in instructions:
        data = DATA_EXPRESSION.match(line)
        assert data is not None
        city1 = graph[data.group(1)]
        city2 = graph[data.group(2)]
        distance = int(data.group(3))
        city1.connections[city2] = distance
        city2.connections[city1] = distance

    return graph


def _travel_path(graph: dict[str, Node], path: tuple) -> int:
    "Travel through a given path and return the total distance it covers. Return 0 if invalid"
    distance = 0

    for city_idx in range(len(path) - 1):
        cur_city = graph[path[city_idx]]
        if cur_city in graph[path[city_idx + 1]].connections:
            distance += graph[path[city_idx + 1]].connections[cur_city]
        else:
            return 0
    return distance


def _get_distance(instructions: list[str], distance_func) -> int:
    "Gather all the distances covered by each Hamiltonian path in the graph. Return one distance using the distance_fun"
    graph = _build_graph(instructions)

    possible_paths = permutations(graph.keys(), len(graph.keys()))

    distances = set()
    for path in possible_paths:
        distance = _travel_path(graph, path)
        if distance:
            distances.add(distance)

    return distance_func(distances)


def part1(instructions: list[str]) -> int:
    "Return the shortest Hamiltonian path in the graph described by the instructions"
    return _get_distance(instructions, min)


def part2(instructions: list[str]) -> int:
    "Return the longest Hamiltonian path in the graph described by the instructions"
    return _get_distance(instructions, max)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_9/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
