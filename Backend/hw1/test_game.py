import unittest
from tic_tac import TicTacGame
from custom_exceptions.exceptions import NotANumberError, OutOfRangeError, OccupiedCellError


class TicTacTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validate_input(self):
        self.assertEqual(self.game.validate_input("9"), 9)
        self.assertRaises(NotANumberError, self.game.validate_input, "one")
        self.assertRaises(NotANumberError, self.game.validate_input, "-1")
        self.game.X_moves = [1, 5]
        self.assertRaises(OccupiedCellError, self.game.validate_input, "5")
        self.assertRaises(OutOfRangeError, self.game.validate_input, "129")

    def test_check_winner(self):
        self.game.X_moves = [1, 2, 6, 3]
        self.assertEqual(self.game.check_winner(), True)
        self.game.X_moves = [1, 2, 6, 9]
        self.assertEqual(self.game.check_winner(), False)

