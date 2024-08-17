import unittest
from game.board import Board, Pawn, Rook, Bishop, Knight, Queen, King

class TestBoard(unittest.TestCase):

    def test_initial_setup(self):
        board = Board()
        
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertIsInstance(board.get_piece(0, 1), Knight)
        self.assertIsInstance(board.get_piece(0, 2), Bishop)
        self.assertIsInstance(board.get_piece(0, 3), King)
        self.assertIsInstance(board.get_piece(0, 4), Queen)
        self.assertIsInstance(board.get_piece(0, 5), Bishop)
        self.assertIsInstance(board.get_piece(0, 6), Knight)
        self.assertIsInstance(board.get_piece(0, 7), Rook)

        for col in range(8):
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertIsInstance(board.get_piece(6, col), Pawn)

        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertIsInstance(board.get_piece(7, 1), Knight)
        self.assertIsInstance(board.get_piece(7, 2), Bishop)
        self.assertIsInstance(board.get_piece(7, 3), King)
        self.assertIsInstance(board.get_piece(7, 4), Queen)
        self.assertIsInstance(board.get_piece(7, 5), Bishop)
        self.assertIsInstance(board.get_piece(7, 6), Knight)
        self.assertIsInstance(board.get_piece(7, 7), Rook)

        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(board.get_piece(row, col))
   
    def test_get_piece(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertEqual(piece.__class__.__name__, 'Rook')
        self.assertEqual(piece.__colour__, 'WHITE')


if __name__ == '__main__':
    unittest.main()