import unittest
from game.pieces import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        self.white_rook = Rook('WHITE')
        self.black_rook = Rook('BLACK')

    def test_rook_symbols(self):
        white_rook = Rook('WHITE')
        black_rook = Rook('BLACK')
        self.assertEqual(white_rook.symbol(), '♖')
        self.assertEqual(black_rook.symbol(), '♜')

    def test_horizontal_move(self):
        self.assertTrue(self.white_rook.move(0, 0, 0, 7))
        self.assertFalse(self.white_rook.move(0, 0, 1, 7))

    def test_vertical_move(self):
        self.assertTrue(self.black_rook.move(0, 0, 7, 0))
        self.assertFalse(self.black_rook.move(0, 0, 7, 1))

    def test_invalid_move(self):
        self.assertFalse(self.white_rook.move(0, 0, 7, 7))
        self.assertFalse(self.black_rook.move(0, 0, 1, 2))



if __name__ == '__main__':
    unittest.main()