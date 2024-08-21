import unittest
from game.pieces import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.white_queen = Queen('WHITE')
        self.black_queen = Queen('BLACK')



if __name__ == '__main__':
    unittest.main()