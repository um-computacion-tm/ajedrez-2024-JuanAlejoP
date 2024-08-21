from game.pieces import *

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook('WHITE')
        self.__positions__[0][1] = Knight('WHITE')
        self.__positions__[0][2] = Bishop('WHITE')
        self.__positions__[0][3] = King('WHITE')
        self.__positions__[0][4] = Queen('WHITE')
        self.__positions__[0][5] = Bishop('WHITE')
        self.__positions__[0][6] = Knight('WHITE')
        self.__positions__[0][7] = Rook('WHITE')

        for col in range(8):
            self.__positions__[1][col] = Pawn('WHITE')
            self.__positions__[6][col] = Pawn('BLACK')

        self.__positions__[7][0] = Rook('BLACK')
        self.__positions__[7][1] = Knight('BLACK')
        self.__positions__[7][2] = Bishop('BLACK')
        self.__positions__[7][3] = King('BLACK')
        self.__positions__[7][4] = Queen('BLACK')
        self.__positions__[7][5] = Bishop('BLACK')
        self.__positions__[7][6] = Knight('BLACK')
        self.__positions__[7][7] = Rook('BLACK')

    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8