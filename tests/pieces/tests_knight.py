import unittest
from game.pieces import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.white_knight = Knight('WHITE')
        self.black_knight = Knight('BLACK')



if __name__ == '__main__':
    unittest.main()