import sys

inputs = sys.stdin.readlines()
board = list()
for _ in range(1, len(inputs)-1):
    board.append(list(inputs[_].rstrip().split()))


def print_board(board):
    for b in board:
        print(' '.join(b))


com_q = list(map(int, inputs[len(inputs)-1].rstrip().split()))
for com in com_q:
    if com == 1:
        board.reverse()
    elif com == 2:
        for i in range(len(board)):
            board[i].reverse()
    elif com == 3:
        new = list()
        for j in range(len(board[0])):
            new.append([board[i][j] for i in range(len(board)-1, -1, -1)])
        board = new
    elif com == 4:
        new = list()
        for j in range(len(board[0])-1, -1, -1):
            new.append([board[i][j] for i in range(len(board))])
        board = new
    elif com == 5:
        n2 = len(board)//2
        m2 = len(board[0])//2
        for i in range(n2):
            for j in range(m2):
                board[i][j], board[i][j+m2], board[i+n2][j+m2], board[i + n2][j]\
                    = board[i+n2][j], board[i][j], board[i][j+m2], board[i+n2][j+m2]
    elif com == 6:
        n2 = len(board)//2
        m2 = len(board[0])//2
        for i in range(n2):
            for j in range(m2):
                board[i][j], board[i][j+m2], board[i+n2][j+m2], board[i + n2][j]\
                    = board[i][j+m2], board[i+n2][j+m2], board[i+n2][j], board[i][j]

print_board(board)
