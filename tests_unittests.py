import unittest
import unittest.mock
from Generic_Space_Game import Game, HeavySoldier, LightSoldier, MeleeSoldier
import random

class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        self.game.load_weapons()

    def test_choose_character(self) -> None:
        for index, soldier_type in enumerate([HeavySoldier, LightSoldier, MeleeSoldier]):
            with unittest.mock.patch('builtins.input', return_value=str(index+1)):
                self.game.choose_character()
                self.assertIsInstance(self.game.player, soldier_type)

    def test_choose_weapons(self) -> None:
        self.game.player = HeavySoldier()
        for i in range(1, 4):
            with unittest.mock.patch('builtins.input', return_value=str(i)):
                weapon = self.game.choose_weapon()
                self.assertIsInstance(weapon, dict)
        
        self.game.player = LightSoldier()
        for i in range(1, 4):
            with unittest.mock.patch('builtins.input', return_value=str(i)):
                weapon = self.game.choose_weapon()
                self.assertIsInstance(weapon, dict)

        self.game.player = MeleeSoldier()
        for i in range(1, 4):
            with unittest.mock.patch('builtins.input', return_value=str(i)):
                weapon = self.game.choose_weapon()
                self.assertIsInstance(weapon, dict)


class SoldierTest(unittest.TestCase):
    
    def setUp(self) -> None:
        game = Game()
        game.load_weapons()
        self.weapon = random.choice(game.weapons)

    def test_attack(self) -> None:
        for soldier in [HeavySoldier(), LightSoldier(), MeleeSoldier()]:
            starting_hp = soldier.current_health
            soldier.attack(weapon=self.weapon, distance_from_player=0)
            self.assertLess(soldier.current_health, starting_hp)

if __name__ == '__main__':
    unittest.main()
