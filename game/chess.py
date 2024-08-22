from game.board import Board, BoardInitializer

class Chess:
    def __init__(self, board_initializer=None):
        self.__board__ = Board()
        if board_initializer is None:
            board_initializer = BoardInitializer()
        board_initializer.initialize(self.__board__)
        self.__turn__ = 'WHITE'
    
    @property
    def board(self):
        return self.__board__

    @property
    def turn(self):
         return self.__turn__

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError('No hay pieza en esa posición.')
        
        if not piece.valid_move(from_row, from_col, to_row, to_col):
            raise ValueError('Movimiento inválido para esta pieza.')

        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.change_turn()

    def change_turn(self):
        self.__turn__ = 'BLACK' if self.__turn__ == 'WHITE' else 'WHITE'