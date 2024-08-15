from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # print(chess.show_board())
        print('Turno: ', chess.turn  )
        from_row = int(input('Fila Inicial: '))
        from_col = int(input('Columna Inicial: '))
        to_row = int(input('Fila Final: '))
        to_col = int(input('Columna Final: '))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )
    except Exception as e:
        print('ERROR!', e)



if __name__ == '__main__':
    main()