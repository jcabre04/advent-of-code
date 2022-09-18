from advent_of_code.year_2015.day_21 import run


class TestPart1:
    def test_part1_player(self) -> None:
        player = run.Player(hitpoints=8, damage=5, armor=5)
        assert player.hitpoints == 8
        assert player.damage == 5
        assert player.armor == 5
        assert player.gold_spent == 0

        weapon = run.Equipment(cost=8, damage=4, armor=0)
        player.equip(weapon)
        assert player.hitpoints == 8
        assert player.damage == 9
        assert player.armor == 5
        assert player.gold_spent == 8

        weapon = run.Equipment(cost=102, damage=0, armor=5)
        player.equip(weapon)
        assert player.hitpoints == 8
        assert player.damage == 9
        assert player.armor == 10
        assert player.gold_spent == 110

        player.unequip_all()
        assert player.hitpoints == 8
        assert player.damage == 5
        assert player.armor == 5
        assert player.gold_spent == 0

        player.hitpoints = 3
        player.heal()
        assert player.hitpoints == 8

    def test_part1_example(self) -> None:
        player = run.Player(hitpoints=8, damage=5, armor=5)
        enemy = run.Enemy(hitpoints=12, damage=7, armor=2)
        assert run.battle(player, enemy)


# class TestPart2:
#     def test_part2_example(self) -> None:
#         assert run.part2([]) == 0
