class ConsoleIO:
    def input_move(self):
        from_pos = input('Mover pieza desde (ej. a2): ').strip().lower()
        to_pos = input('A casilla (ej. a3): ').strip().lower()
        
        from_row, from_col = self.algebraic_to_index(from_pos)
        to_row, to_col = self.algebraic_to_index(to_pos)

        return from_row, from_col, to_row, to_col

    def algebraic_to_index(self, pos):
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        col = col_map[pos[0]]
        row = int(pos[1]) - 1
        return row, col

    def output_turn(self, turn):
        print(f'Turno: {turn}')

    def output_error(self, error_message):
        print('ERROR!', error_message)

    def output_board(self, board):
        print(board)