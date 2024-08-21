import unittest
from game.pieces import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.white_king = King('WHITE')
        self.black_king = King('BLACK')



if __name__ == '__main__':
    unittest.main()