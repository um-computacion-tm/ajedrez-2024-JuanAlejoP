import unittest
from game.pieces import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.white_bishop = Bishop('WHITE')
        self.black_bishop = Bishop('BLACK')

    def test_diagonal_move(self):
        self.assertTrue(self.white_bishop.move(0, 2, 3, 5))
        self.assertTrue(self.black_bishop.move(7, 2, 4, 5))

    def test_invalid_move(self):
        self.assertFalse(self.white_bishop.move(0, 2, 0, 5))
        self.assertFalse(self.black_bishop.move(7, 2, 7, 0))



if __name__ == '__main__':
    unittest.main()