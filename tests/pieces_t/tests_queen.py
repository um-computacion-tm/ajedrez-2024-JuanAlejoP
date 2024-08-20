import unittest
from game.pieces import Queen

class TestQueenMovement(unittest.TestCase):

    def setUp(self):
        self.white_queen = Queen('WHITE')
        self.black_queen = Queen('BLACK')

    def test_valid_diagonal_move(self):
        self.assertTrue(self.white_queen.valid_move(0, 0, 7, 7))
        self.assertTrue(self.black_queen.valid_move(7, 7, 0, 0))

    def test_valid_horizontal_move(self):
        self.assertTrue(self.white_queen.valid_move(0, 0, 0, 7))
        self.assertTrue(self.black_queen.valid_move(7, 7, 7, 0))

    def test_valid_vertical_move(self):
        self.assertTrue(self.white_queen.valid_move(0, 0, 7, 0))
        self.assertTrue(self.black_queen.valid_move(7, 7, 0, 7))

    def test_invalid_move(self):
        self.assertFalse(self.white_queen.valid_move(0, 0, 6, 7))
        self.assertFalse(self.black_queen.valid_move(7, 7, 5, 6))