import unittest
from game.chess import Chess
from game.pieces import Pawn

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_move_piece(self):
        self.chess.move(1, 0, 2, 0)
        piece = self.chess.board.get_piece(2, 0)
        self.assertIsInstance(piece, Pawn)
        self.assertIsNone(self.chess.board.get_piece(1, 0))
    
    def test_no_piece_error(self):
        with self.assertRaises(ValueError):
            self.chess.move(3, 3, 4, 4)

    def test_change_turn(self):
        self.chess.move(1, 0, 2, 0)
        self.assertEqual(self.chess.turn, 'BLACK')
        self.chess.move(6, 0, 5, 0)
        self.assertEqual(self.chess.turn, 'WHITE')


if __name__ == '__main__':
    unittest.main()