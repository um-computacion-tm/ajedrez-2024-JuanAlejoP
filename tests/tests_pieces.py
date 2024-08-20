import unittest
from game.pieces import Rook, Queen, King

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


if __name__ == '__main__':
    unittest.main()