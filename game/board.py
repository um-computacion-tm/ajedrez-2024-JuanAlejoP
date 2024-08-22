from game.pieces import *

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece: Piece, row, col):
        self.__positions__[row][col] = piece

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if not self.within_bounds(to_row, to_col):
            raise ValueError('Movimiento fuera de los límites.')
        
        self.place_piece(piece, to_row, to_col)
        self.__positions__[from_row][from_col] = None

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            row_str = "|"
            for piece in row:
                if piece is None:
                    row_str += "   |"
                else:
                    row_str += f" {piece} |"
            board_str += row_str + "\n" + "-" * 33 + "\n"
        return board_str
    
class BoardInitializer:
    def __init__(self):
        self.white_back_row = [
            Rook('WHITE'), Knight('WHITE'), Bishop('WHITE'), 
            King('WHITE'), Queen('WHITE'), Bishop('WHITE'), 
            Knight('WHITE'), Rook('WHITE')
        ]
        self.black_back_row = [
            Rook('BLACK'), Knight('BLACK'), Bishop('BLACK'), 
            King('BLACK'), Queen('BLACK'), Bishop('BLACK'), 
            Knight('BLACK'), Rook('BLACK')
        ]

    def initialize(self, board: Board):
        for col, piece in enumerate(self.white_back_row):
            board.place_piece(piece, 0, col)

        for col in range(8):
            board.place_piece(Pawn('WHITE'), 1, col)

        for col in range(8):
            board.place_piece(Pawn('BLACK'), 6, col)

        for col, piece in enumerate(self.black_back_row):
            board.place_piece(piece, 7, col)