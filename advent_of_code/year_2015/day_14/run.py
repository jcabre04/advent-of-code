from re import compile, match


DATA_EXPRESSION = compile(r"(\w+) can fly (\d+) km/s for (\d+) s.+ (\d+) seconds\.")


class Reindeer:
    "Represents one of Santa's reindeer"

    def __init__(self, speed: int, stamina: int, rest_period: int) -> None:
        self.distance = 0  # The total distance this reindeer traveled
        self.speed = speed  # km per second
        self.stamina = stamina  # how many seconds the reindeer travels before resting
        self.cur_stamina = stamina  # current stamina
        self.rest_period = rest_period  # how many seconds the reindeer rests for
        self.rest_left = 0  # how much longer the reindeer must rest before flying again
        self.resting = False
        self.score = 0

    def step(self) -> None:
        if self.resting:
            self.rest_left -= 1

            if self.rest_left == 0:
                self.resting = False
                self.cur_stamina = self.stamina
        else:
            self.cur_stamina -= 1
            self.distance += self.speed

            if self.cur_stamina == 0:
                self.resting = True
                self.rest_left = self.rest_period


def _create_reindeers(instructions: list[str]) -> dict[str, Reindeer]:
    "Extract data from instructions to create all Reindeers and return dictionary of them"
    reindeers = {}
    for line in instructions:
        data = match(DATA_EXPRESSION, line)
        assert data is not None
        speed = int(data.group(2))
        stamina = int(data.group(3))
        rest_period = int(data.group(4))
        reindeers[data.group(1)] = Reindeer(speed, stamina, rest_period)

    return reindeers


def _get_furthest(reindeers: dict[str, Reindeer]) -> list[Reindeer]:
    "Returns a list of all the reindeer with the furtherst distance"
    distance = max(reindeers.values(), key=lambda racer: racer.distance).distance
    return [racer for racer in reindeers.values() if racer.distance == distance]


def part1(instructions: list[str], simulation_time: int) -> int:
    "Simulate reindeer's flying for and return the farthest distance"
    reindeers = _create_reindeers(instructions)
    for _ in range(simulation_time):
        for racer in reindeers.values():
            racer.step()

    return _get_furthest(reindeers)[0].distance


def part2(instructions: list[str], simulation_time) -> int:
    "Simulate reindeer's flying for and return the highest score"
    reindeers = _create_reindeers(instructions)
    for _ in range(simulation_time):
        for racer in reindeers.values():
            racer.step()
        for racer in _get_furthest(reindeers):
            racer.score += 1

    return max(reindeers.values(), key=lambda racer: racer.score).score


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_14/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions, 2503)}")
    print(f"Part 2: {part2(instructions, 2503)}")
