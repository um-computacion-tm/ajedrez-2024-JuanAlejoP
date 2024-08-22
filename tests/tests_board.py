import unittest
from game.board import Board, Pawn, Rook, Bishop, Knight, Queen, King, BoardInitializer

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        initializer = BoardInitializer()
        initializer.initialize(self.board)

    def test_initial_setup(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), King)
        self.assertIsInstance(self.board.get_piece(0, 4), Queen)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)

        for row in range(8):
            for col in range(8):
                if row == 1 or row == 6:
                    self.assertIsInstance(self.board.get_piece(row, col), Pawn)
                elif 2 <= row <= 5:
                    self.assertIsNone(self.board.get_piece(row, col))

        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 3), King)
        self.assertIsInstance(self.board.get_piece(7, 4), Queen)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
   
    def test_get_piece(self):
        piece = self.board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.colour, 'WHITE')

    def test_within_bounds(self):
        ...



if __name__ == '__main__':
    unittest.main()