import unittest
from game.pieces import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.white_king = King('BLANCAS')
        self.black_king = King('NEGRAS')

    def test_king_symbols(self):
        white_king = King('BLANCAS')
        black_king = King('NEGRAS')
        self.assertEqual(white_king.symbol(), '♚')
        self.assertEqual(black_king.symbol(), '♚')

    def test_single_square_move(self):
        self.assertTrue(self.white_king.move(4, 4, 4, 5))
        self.assertTrue(self.black_king.move(4, 4, 5, 4))

    def test_invalid_move(self):
        self.assertFalse(self.white_king.move(4, 4, 6, 4))
        self.assertFalse(self.black_king.move(4, 4, 4, 6))


if __name__ == '__main__':
    unittest.main()