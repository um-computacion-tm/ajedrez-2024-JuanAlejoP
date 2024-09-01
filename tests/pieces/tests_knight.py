import unittest
from game.pieces import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.white_knight = Knight('WHITE')
        self.black_knight = Knight('BLACK')

    def test_knight_symbols(self):
        white_knight = Knight('WHITE')
        black_knight = Knight('BLACK')
        self.assertEqual(white_knight.symbol(), '♞')
        self.assertEqual(black_knight.symbol(), '♞')

    def test_l_shape_move(self):
        self.assertTrue(self.white_knight.move(1, 0, 2, 2))
        self.assertTrue(self.black_knight.move(7, 1, 5, 2))

    def test_invalid_move(self):
        self.assertFalse(self.white_knight.move(0, 1, 0, 0))
        self.assertFalse(self.black_knight.move(7, 1, 0, 0))



if __name__ == '__main__':
    unittest.main()