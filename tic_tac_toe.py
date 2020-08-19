import random

board = [' ' for x in range(10)]

def print_board(board):
    print(board[1], ' |', board[2], ' |', board[3])
    print('--', '+', '--', '+', '--')
    print(board[4], ' |', board[5], ' |', board[6])
    print('--', '+', '--', '+', '--')
    print(board[7], ' |', board[8], ' |', board[9])

def full_board():
    if board.count(' ') > 1:
        return
    else:
        print("It's a tie")
        quit()

def check_win():
    if (board[1] == 'x' and board[2] == 'x' and board[3] == 'x') or (board[4] == 'x' and board[5] == 'x' and board[6] == 'x') or (board[7] == 'x' and board[8] == 'x' and board[9] == 'x') or (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') or (board[3] == 'x' and board[6] == 'x' and board[9] == 'x') or (board[1] == 'x' and board[5] == 'x' and board[9] == 'x') or (board[3] == 'x' and board[5] == 'x' and board[7] == 'x'):
        print('You win! congrats')
        quit()
    elif (board[1] == 'o' and board[2] == 'o' and board[3] == 'o') or (board[4] == 'o' and board[5] == 'o' and board[6] == 'o') or (board[7] == 'o' and board[8] == 'o' and board[9] == 'o') or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o') or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o') or (board[3] == 'o' and board[6] == 'o' and board[9] == 'o') or (board[1] == 'o' and board[5] == 'o' and board[9] == 'o') or (board[3] == 'o' and board[5] == 'o' and board[7] == 'o'):
        print('The computer won')
        quit()
    else:
        return

def player_move(move):

    if board[move] == ' ' and move >= 1 and move <= 9:
        board[move] = 'x'
        return move
    else:
        print('Invalid move')
        main()

def pc_move(move):
    move = random.randrange(1, 10)
    if board[move] == ' ':
        board[move] =  'o'
        return move
    else:
        pc_move(move)

def ai(move):
    pass

def main():

    check_win()
    full_board()
    move = int(input("A quina posició tires? 1-9"))
    player_move(move)
    print_board(board)
    print("\n")
    pc_move(move)
    print_board(board)
    print("\n")

    main()

def main2():

    check_win()
    full_board()
    move = int(input("A quina posició tires? 1-9   "))
    player_move(move)
    print_board(board)
    print("\n")
    ai(move)
    print_board(board)
    print("\n")

    main2()


def version():
    version = str(input("Vols jugar a la versió fàcil o a la difícil? (f/d)"))

    if version.lower() == 'f':
        print('fàcil')
        main()
    elif version.lower() == 'd':
        print('dificil')
        main2()
    else:
        print('Invàlid')
        version()

version()