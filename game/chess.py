from game.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = ''
        ...
    
    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
             raise ValueError('No hay pieza en esa posición.')
        
        self.__board__.__positions__[to_row][to_col] = piece
        self.__board__.__positions__[from_row][from_col] = None

        self.change_turn()

    @property
    def turn(self):
         return self.__turn__

    def change_turn(self):
            if self.__turn__ == 'WHITE':
                self.__turn__ = 'BLACK'
            else:
                 self.__turn__ = 'WHITE'