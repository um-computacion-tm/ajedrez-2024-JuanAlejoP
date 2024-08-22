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

    def output_board(self, board):
        print(board)