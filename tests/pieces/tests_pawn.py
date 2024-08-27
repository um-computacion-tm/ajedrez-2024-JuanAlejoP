import unittest
from game.pieces import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn('WHITE')
        self.black_pawn = Pawn('BLACK')

    def test_pawn_symbols(self):
        white_pawn = Pawn('WHITE')
        black_pawn = Pawn('BLACK')
        self.assertEqual(white_pawn.symbol(), '♙')
        self.assertEqual(black_pawn.symbol(), '♟')

    def test_pawn_initial_double_step(self):
        self.assertTrue(self.white_pawn.move(1, 0, 3, 0))
        self.assertTrue(self.black_pawn.move(6, 0, 4, 0))

    def test_pawn_single_step(self):
        self.assertTrue(self.white_pawn.move(2, 0, 3, 0))
        self.assertTrue(self.black_pawn.move(5, 0, 4, 0))

    def test_pawn_capture(self):
        self.assertTrue(self.white_pawn.move(4, 4, 5, 5))
        self.assertTrue(self.black_pawn.move(3, 3, 2, 2))

    def test_pawn_invalid_move(self):
        self.assertFalse(self.white_pawn.move(1, 0, 3, 1))
        self.assertFalse(self.black_pawn.move(6, 0, 4, 1))



if __name__ == '__main__':
    unittest.main()