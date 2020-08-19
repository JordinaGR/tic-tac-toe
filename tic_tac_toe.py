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
        end_game()

def check_win():
    pass

def player_move(move):

    if board[move] == ' ' and move >= 1 and move <= 9:
        board[move] = 'X'
        return move
    else:
        print('Invalid move')
        main()


def pc_move(move):
    move = 3
    if board[move] == ' ':
        board[move] =  'O'
        return move
    else:
        move = 4
        board[move] = 'O'
        return move

def end_game():
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

main()