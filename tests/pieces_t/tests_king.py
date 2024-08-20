import unittest
from game.pieces import King

class TestKingMovement(unittest.TestCase):

    def setUp(self):
        self.white_king = King('WHITE')
        self.black_king = King('BLACK')

    def test_valid_move(self):
        self.assertTrue(self.white_king.valid_move(4, 4, 5, 5))
        self.assertTrue(self.black_king.valid_move(4, 4, 3, 3))

    def test_invalid_move(self):
        self.assertFalse(self.white_king.valid_move(4, 4, 6, 6))
        self.assertFalse(self.black_king.valid_move(4, 4, 2, 2))

    def test_edge_of_board(self):
        with self.assertRaises(ValueError):
            self.white_king.valid_move(7, 7, 8, 8)
        with self.assertRaises(ValueError):
            self.black_king.valid_move(0, 0, -1, -1)