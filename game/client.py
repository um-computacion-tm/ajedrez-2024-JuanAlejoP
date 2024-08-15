from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        from_row = int(input('From Row: '))
        from_col = int(input('From Col: '))
        to_row = int('To Row: ')
        to_col = int(input('To Col: '))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )
    except Exception as e:
        print('ERROR!')



if __name__ == '__main__':
    main()