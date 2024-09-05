import unittest
from game.chess import Chess
from game.pieces import Pawn, King, Knight

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess.turn, 'BLANCAS')

    def test_move(self):
        self.chess.move(1, 0, 3, 0)
        self.assertIsInstance(self.chess.board.get_piece(3, 0), Pawn)
        self.assertIsNone(self.chess.board.get_piece(1, 0))
        self.assertEqual(self.chess.turn, 'NEGRAS')

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
        self.assertEqual(self.chess.board.get_piece(4, 1).colour, 'BLANCAS')

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

    def test_knight_move(self):
        knight = self.chess.board.get_piece(0, 1)
        self.assertTrue(self.chess.is_valid_move(knight, 0, 1, 2, 2))
        self.assertFalse(self.chess.is_valid_move(knight, 0, 1, 3, 3))

    def test_turn_change(self):
        self.assertEqual(self.chess.turn, 'BLANCAS')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'NEGRAS')
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, 'BLANCAS')

    def test_capture_king(self):
        self.chess.move(1, 3, 3, 3)
        self.chess.move(6, 5, 5, 5)
        self.chess.move(0, 3, 2, 3)
        self.chess.move(7, 4, 6, 5)
        self.chess.move(2, 3, 5, 6)
        self.chess.move(6, 5, 7, 4)
        self.chess.move(5, 6, 7, 4)
        self.assertTrue(self.chess.game_over)


if __name__ == '__main__':
    unittest.main()