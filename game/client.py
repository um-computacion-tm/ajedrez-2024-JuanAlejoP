from game.chess import Chess

class ConsoleIO:
    def input_move(self):
        from_row = int(input('Fila Inicial: '))
        from_col = int(input('Columna Inicial: '))
        to_row = int(input('Fila Final: '))
        to_col = int(input('Columna Final: '))
        return from_row, from_col, to_row, to_col

    def output_turn(self, turn):
        print(f'Turno: {turn}')

    def output_error(self, error_message):
        print('ERROR!', error_message)

class Game:
    def __init__(self, chess: Chess, io_handler: ConsoleIO):
        self.chess = chess
        self.io_handler = io_handler

    def play(self):
        try:
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