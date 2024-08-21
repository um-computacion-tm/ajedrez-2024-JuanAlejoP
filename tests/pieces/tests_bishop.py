import unittest
from game.pieces import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.white_bishop = Bishop('WHITE')
        self.black_bishop = Bishop('BLACK')



if __name__ == '__main__':
    unittest.main()