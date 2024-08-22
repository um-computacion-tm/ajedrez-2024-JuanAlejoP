import unittest
from game.chess import Chess
from game.pieces import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_move_piece(self):
        self.chess.move(0, 0, 0, 3)
        piece = self.chess.board.get_piece(0, 3)
        self.assertIsInstance(piece, Rook)
        self.assertIsNone(self.chess.board.get_piece(0, 0))
    
    def test_no_piece_error(self):
        with self.assertRaises(ValueError):
            self.chess.move(3, 3, 4, 4)

    def test_change_turn(self):
        self.chess.move(0, 0, 0, 3)
        self.assertEqual(self.chess.turn, 'BLACK')
        self.chess.move(7, 0, 7, 3)
        self.assertEqual(self.chess.turn, 'WHITE')



if __name__ == '__main__':
    unittest.main()