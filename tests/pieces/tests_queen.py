import unittest
from game.pieces import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.white_queen = Queen('WHITE')
        self.black_queen = Queen('BLACK')

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