from itertools import product
from re import search
from typing import Callable


class Ingredient:
    "Represents one type of ingredient"

    def __init__(
        self, capacity: int, durability: int, flavor: int, texture: int, calories: int
    ) -> None:
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def scale(self, amount: int) -> tuple[int, int, int, int, int]:
        "Return a tuple containing the ingredient's values multiplied by the amount (teaspoons)"
        return (
            self.capacity * amount,
            self.durability * amount,
            self.flavor * amount,
            self.texture * amount,
            self.calories * amount,
        )


def _create_ingredients(instructions: list[str]) -> dict[str, Ingredient]:
    "Extract information from instrucations to create and return a list of Ingredients"
    ingredients = {}
    for line in instructions:
        data = search(
            r"(\w+): .* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+), .* (-?\d+)",
            line,
        )
        assert data is not None
        name, cap, dur, fla, tex, cal = data.groups()
        ingredients[name] = Ingredient(int(cap), int(dur), int(fla), int(tex), int(cal))

    return ingredients


def _mult_part1(nums: list[int]) -> int:
    "Return the product of multiplying all elements in the list"
    total = 1
    for n in nums[:4]:
        total = 0 if n < 0 else total * n

    return total


def _mult_part2(nums: list[int]) -> int:
    "Same as _mult_part1 except that lists (cookies) must have 500 for their last element (calories)"
    total = 1
    if nums[4] != 500:
        return 0

    for n in nums[:4]:
        total = 0 if n < 0 else total * n

    return total


def _add_ingredient_to_cookie(cookie: list[int], ingredient: tuple[int, ...]) -> None:
    "Add the properties of the ingredient(list) to the cookie (list)"
    for idx, t_num in enumerate(ingredient):
        cookie[idx] += t_num


def _get_highest_score(
    ingredients: dict[str, Ingredient],
    possible_amounts: list[tuple[int, ...]],
    mult: Callable,
) -> int:
    "Returns the highest score produced by the cookies made with all possible amounts of ingredients"
    highest_score = 0
    for amounts in possible_amounts:
        cookie_properties = [0] * 5
        for teaspoons, ingr in zip(amounts, ingredients.values()):
            _add_ingredient_to_cookie(cookie_properties, ingr.scale(teaspoons))

        cookie_score = mult(cookie_properties)

        if cookie_score > highest_score:
            highest_score = cookie_score

    return highest_score


def _get_possible_amounts(ingredient_count: int) -> list[tuple[int, ...]]:
    "Return the possible amounts that each ingredient could be, satisfying the weight restriction"
    teaspoon_range = [amount for amount in range(1, 98)]
    return [
        amount_list
        for amount_list in product(teaspoon_range, repeat=ingredient_count)
        if sum(amount_list) == 100
    ]


def part1(instructions: list[str]) -> int:
    "Using the ingredients from the instructions, return the highest score of all ingredients combinations"
    ingredients = _create_ingredients(instructions)
    possible_amounts = _get_possible_amounts(len(ingredients))
    return _get_highest_score(ingredients, possible_amounts, _mult_part1)


def part2(instructions: list[str]) -> int:
    "Same as part 1 except that the resulting cookie must have 500 calories exactly"
    ingredients = _create_ingredients(instructions)
    possible_amounts = _get_possible_amounts(len(ingredients))
    return _get_highest_score(ingredients, possible_amounts, _mult_part2)


if __name__ == "__main__":
    input_file = "advent_of_code/year_2015/day_15/input.txt"
    with open(input_file, "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
