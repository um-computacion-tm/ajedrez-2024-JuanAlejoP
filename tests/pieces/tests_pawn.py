import unittest
from game.pieces import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn('WHITE')
        self.black_pawn = Pawn('BLACK')



if __name__ == '__main__':
    unittest.main()