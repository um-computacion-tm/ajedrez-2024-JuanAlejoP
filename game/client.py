from game.chess import Chess
from game.console_io import ConsoleIO

class Game:
    def __init__(self, chess: Chess, io_handler: ConsoleIO):
        self.chess = chess
        self.io_handler = io_handler

    def play(self):
        try:
            self.io_handler.output_board(self.chess.board)
            self.io_handler.output_turn(self.chess.turn)
            from_row, from_col, to_row, to_col = self.io_handler.input_move()
            self.chess.move(from_row, from_col, to_row, to_col)
        except Exception as e:
            self.io_handler.output_error(str(e))

def main():
    chess = Chess()
    io_handler = ConsoleIO()
    game = Game(chess, io_handler)
    while True:
        game.play()



if __name__ == '__main__':
    main()