import random
import sys

sys.setrecursionlimit(25000)

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

def check_win(bo, le):
    if (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or(bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or(bo[9] == le and bo[5] == le and bo[1] == le):
        print("Has won the ", le, "'s")
        quit()
    else:
        return

def check_win2(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or(bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or(bo[9] == le and bo[5] == le and bo[1] == le)

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
    
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
    move = 0
    for let in ['o','x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if check_win2(boardCopy, let):
                move = i
                board[i] = 'o'
                return move

    if board[5] == ' ':
        board[5] = 'o'
        move = 5
        return move

    corners = [1, 3, 7, 9]
    for i in corners:
        if board[i] == ' ':
            board[i] = 'o'
            move = i
            return move

    edges = [2, 4, 6, 8]
    for i in edges:
        if board[i] == ' ':
            board[i] = 'o'
            move = i
            return move
            
def main():

    check_win(board, 'x')
    check_win(board, 'o')
    full_board()
    move = int(input("A quina posició tires? 1-9   "))
    player_move(move)
    print_board(board)
    print("\n")
    pc_move(move)
    print_board(board)
    print("\n")

    main()

def main2():

    check_win(board, 'x')
    check_win(board, 'o')
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
    version = str(input("Vols jugar a la versió fàcil o a la difícil? (f/d)   "))

    if version.lower() == 'f':
        main()
    elif version.lower() == 'd':
        main2()
    else:
        print('Invàlid')
        version()

version()