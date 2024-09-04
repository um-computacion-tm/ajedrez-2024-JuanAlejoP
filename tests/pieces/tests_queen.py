import unittest
from game.pieces import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.white_queen = Queen('BLANCAS')
        self.black_queen = Queen('NEGRAS')

    def test_queen_symbols(self):
        white_queen = Queen('BLANCAS')
        black_queen = Queen('NEGRAS')
        self.assertEqual(white_queen.symbol(), '♛')
        self.assertEqual(black_queen.symbol(), '♛')

    def test_horizontal_vertical_move(self):
        self.assertTrue(self.white_queen.move(0, 0, 0, 7))
        self.assertTrue(self.black_queen.move(0, 0, 7, 0))

    def test_diagonal_move(self):
        self.assertTrue(self.white_queen.move(0, 0, 7, 7))
        self.assertTrue(self.black_queen.move(7, 7, 0, 0))

    def test_invalid_move(self):
        self.assertFalse(self.white_queen.move(0, 0, 2, 1))
        self.assertFalse(self.black_queen.move(7, 7, 5, 6))



if __name__ == '__main__':
    unittest.main()