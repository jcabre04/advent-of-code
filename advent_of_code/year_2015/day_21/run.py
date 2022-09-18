from itertools import combinations, product
from typing import Callable


class Equipment:
    "Represents one piece of Equipment"

    def __init__(self, cost: int, damage: int, armor: int, name: str = "") -> None:
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.name = name

    def __repr__(self) -> str:
        return f"N: {self.name} | C {self.cost}"


class Player:
    "Represents the Player"

    def __init__(
        self, hitpoints: int, damage: int, armor: int, gold_spent: int = 0
    ) -> None:
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor
        self.gold_spent = gold_spent

        self.natural_hitpoints = hitpoints
        self.natural_damage = damage
        self.natural_armor = armor
        self.natural_gold_spent = gold_spent

    def equip(self, equip: Equipment) -> None:
        "Adds the values of the Equipment to the Player"
        self.damage += equip.damage
        self.armor += equip.armor
        self.gold_spent += equip.cost

    def heal(self) -> None:
        "Set Player's hitpoints to their max"
        self.hitpoints = self.natural_hitpoints

    def unequip_all(self) -> None:
        "Resets Player's equipment to their natural values"
        self.damage = self.natural_damage
        self.armor = self.natural_armor
        self.gold_spent = self.natural_gold_spent


class Enemy:
    "Represents one enemy"

    def __init__(self, hitpoints: int, damage: int, armor: int) -> None:
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor

        self.natural_hitpoints = hitpoints

    def heal(self) -> None:
        "Set Enemy's hitpoints to their max"
        self.hitpoints = self.natural_hitpoints


def battle(player: Player, enemy: Enemy) -> bool:
    "Returns True if the Player wins the battle. False otherwise. Damage persists"
    wins = False

    while True:
        # Player attacks the enemy
        enemy.hitpoints -= max(player.damage - enemy.armor, 1)
        if enemy.hitpoints <= 0:
            wins = True
            break

        # Enemy attacks the player
        player.hitpoints -= max(enemy.damage - player.armor, 1)
        if player.hitpoints <= 0:
            wins = False
            break

    return wins


def _get_shop() -> tuple[
    tuple[Equipment, ...], tuple[Equipment, ...], tuple[Equipment, ...]
]:
    "Return the weapons, armor, and rings in the shop. Hard-coded per the puzzle instructions"
    weapons = (
        # Per puzzle, must buy one weapon
        Equipment(name="Dagger", cost=8, damage=4, armor=0),
        Equipment(name="Shortsword", cost=10, damage=5, armor=0),
        Equipment(name="Warhammer", cost=25, damage=6, armor=0),
        Equipment(name="Longsword", cost=40, damage=7, armor=0),
        Equipment(name="Greataxe", cost=74, damage=8, armor=0),
    )

    armor = (
        Equipment(name="No Armor", cost=0, damage=0, armor=0),
        Equipment(name="Leather", cost=13, damage=0, armor=1),
        Equipment(name="Chainmail", cost=31, damage=0, armor=2),
        Equipment(name="Splintmail", cost=53, damage=0, armor=3),
        Equipment(name="Bandedmail", cost=75, damage=0, armor=4),
        Equipment(name="Platemail", cost=102, damage=0, armor=5),
    )

    rings = (
        Equipment(name="Empty Hand Left", cost=0, damage=0, armor=0),
        Equipment(name="Empty Hand Right", cost=0, damage=0, armor=0),
        Equipment(name="Damage +1", cost=25, damage=1, armor=0),
        Equipment(name="Damage +2", cost=50, damage=2, armor=0),
        Equipment(name="Damage +3", cost=100, damage=3, armor=0),
        Equipment(name="Defense +1", cost=20, damage=0, armor=1),
        Equipment(name="Defense +2", cost=40, damage=0, armor=2),
        Equipment(name="Defense +3", cost=80, damage=0, armor=3),
    )

    return weapons, armor, rings


def _find_cost(cost_limit: int, battle_state: bool, cost_comparison: Callable) -> int:
    """
    Iterates over all possible equipment lists.
    If a list reaches the desired battle state, compares the list cost against the given limit.
    Return the best cost per the given cost comparison function
    """
    weapons, armor, rings = _get_shop()
    player = Player(hitpoints=100, damage=0, armor=0)  # Values per puzzle instructions
    boss = Enemy(hitpoints=104, damage=8, armor=1)  # Values per puzzle input
    cost = cost_limit

    all_possible_equip_lists = product(weapons, armor, combinations(rings, r=2))

    for equip_list in all_possible_equip_lists:
        player.unequip_all()
        player.heal()
        boss.heal()

        for equipment in equip_list:
            if isinstance(equipment, tuple):
                ring1, ring2 = equipment
                player.equip(ring1)
                player.equip(ring2)
            else:
                player.equip(equipment)

        if battle(player, boss) is battle_state:
            cost = cost_comparison(cost, player.gold_spent)

    return cost


def part1() -> int:
    "Returns the least amount of gold needed to equip the Player and win against the boss Enemy"

    # Since this function needs to find a minimum, set the limit to an impossibly high value
    return _find_cost(2**20, True, min)


def part2() -> int:
    "Inverse of part 1. Returns the most gold the Player can spend and still lose against the boss Enemy."

    # Since this function needs to find a maximum non-negative value, set the limit to 0
    return _find_cost(0, False, max)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
