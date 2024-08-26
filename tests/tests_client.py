import unittest
from unittest.mock import MagicMock, patch
from game.client import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.mock_chess = MagicMock()
        self.mock_io_handler = MagicMock()
        self.game = Game(self.mock_chess, self.mock_io_handler)

    def test_play_successful_move(self):
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        
        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn)
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_not_called()

    def test_play_with_exception(self):
        self.mock_io_handler.input_move.return_value = (0, 0, 1, 0)
        self.mock_chess.move.side_effect = Exception('Invalid move')

        self.game.play()

        self.mock_io_handler.output_board.assert_called_once_with(self.mock_chess.board)
        self.mock_io_handler.output_turn.assert_called_once_with(self.mock_chess.turn)
        self.mock_io_handler.input_move.assert_called_once()
        self.mock_chess.move.assert_called_once_with(0, 0, 1, 0)
        self.mock_io_handler.output_error.assert_called_once_with('Invalid move')



if __name__ == '__main__':
    unittest.main()