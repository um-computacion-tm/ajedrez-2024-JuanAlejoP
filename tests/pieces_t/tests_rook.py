import unittest
from game.pieces import Rook

class TestRookMovement(unittest.TestCase):

    def setUp(self):
        self.white_rook = Rook('WHITE')
        self.black_rook = Rook('BLACK')

    def test_horizontal_move(self):
        self.assertTrue(self.white_rook.valid_move(0, 0, 0, 7))
        self.assertFalse(self.white_rook.valid_move(0, 0, 1, 7))

    def test_vertical_move(self):
        self.assertTrue(self.black_rook.valid_move(0, 0, 7, 0))
        self.assertFalse(self.black_rook.valid_move(0, 0, 7, 1))

    def test_invalid_move(self):
        self.assertFalse(self.white_rook.valid_move(0, 0, 7, 7))
        self.assertFalse(self.black_rook.valid_move(0, 0, 1, 2))