import unittest
from game.pieces import Piece

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.white_piece = Piece('WHITE')
        self.black_piece = Piece('BLACK')
        
    def test_init(self):
        self.assertEqual(self.white_piece.__colour__, 'WHITE')
        self.assertEqual(self.black_piece.__colour__, 'BLACK')

if __name__ == '__main__':
    unittest.main()