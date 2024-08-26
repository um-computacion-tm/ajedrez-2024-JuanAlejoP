import unittest
from game.chess import Chess
from game.pieces import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess.turn, 'WHITE')

    def test_move(self):
        self.chess.move(1, 0, 3, 0)
        self.assertIsInstance(self.chess.board.get_piece(3, 0), Pawn)
        self.assertIsNone(self.chess.board.get_piece(1, 0))
        self.assertEqual(self.chess.turn, 'BLACK')

    def test_invalid_move_empty_square(self):
        with self.assertRaises(ValueError):
            self.chess.move(3, 3, 4, 3)

    def test_invalid_move_blocked_path(self):
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 0, 3)

    def test_capture(self):
        self.chess.move(1, 0, 3, 0)
        self.chess.move(6, 1, 4, 1)
        self.chess.move(3, 0, 4, 1)
        self.assertIsInstance(self.chess.board.get_piece(4, 1), Pawn)
        self.assertEqual(self.chess.board.get_piece(4, 1).colour, 'WHITE')

    def test_invalid_capture_same_color(self):
        with self.assertRaises(ValueError):
            self.chess.move(0, 0, 0, 1)

    def test_pawn_double_step(self):
        self.assertTrue(self.chess.is_valid_pawn_move(self.chess.board.get_piece(1, 0), 1, 0, 3, 0))
        self.assertFalse(self.chess.is_valid_pawn_move(self.chess.board.get_piece(1, 0), 1, 0, 4, 0))

    def test_pawn_diagonal_capture(self):
        self.chess.move(1, 0, 3, 0)
        self.chess.move(6, 1, 4, 1)
        self.assertTrue(self.chess.is_valid_pawn_move(self.chess.board.get_piece(3, 0), 3, 0, 4, 1))

    def test_turn_change(self):
        self.assertEqual(self.chess.turn, 'WHITE')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'BLACK')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'WHITE')



if __name__ == '__main__':
    unittest.main()