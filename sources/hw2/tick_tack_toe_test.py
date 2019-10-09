#!/usr/bin/env python3
# coding: utf-8

import unittest
from tick_tack_toe import TickTackToe


class TickTackToeTest(unittest.TestCase):

    def setUp(self):
        self.game_instance = TickTackToe()

    def test_change_turn(self):
        self.assertEqual(self.game_instance.get_current_player(), TickTackToe.first_player)
        self.game_instance.change_turn()
        self.assertEqual(self.game_instance.get_current_player(), TickTackToe.second_player)
        self.game_instance.change_turn()
        self.assertEqual(self.game_instance.get_current_player(), TickTackToe.first_player)

    def test_validation(self):
        self.assertEqual(self.game_instance.validate_input('5').good(), True)
        self.assertEqual(self.game_instance.validate_input('10').bad(), True)
        self.assertEqual(self.game_instance.validate_input('10').good(), False)
        self.assertEqual(self.game_instance.validate_input('-').bad(), True)
        self.assertEqual(self.game_instance.validate_input('').bad(), True)
        self.assertEqual(self.game_instance.validate_input('a').bad(), True)

        self.game_instance.set_entity(5)
        self.assertEqual(self.game_instance.validate_input('5').good(), False)


if __name__ == '__main__':
    unittest.main()
