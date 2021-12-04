import sys

inputs = sys.stdin.readlines()
board = list()
for _ in range(len(inputs)):
    board.append(list(inputs[_].rstrip().split()))


def deepcopy(list_2d):
    ret = list()
    for l in list_2d:
        ret.append(l[::])
    return ret


def print_board(board, q):
    print(q)
    for b in board:
        print(' '.join(b))
    print('--------------------------')


default = deepcopy(board)
com_q = list()
while True:
    print_board(board, com_q)
    print("command?(0~6, else=end):", end='')
    com = input()
    if com.isdigit():
        com = int(com)
        if not (0 <= com <= 6):
            break
    else:
        break
    com_q.append(com)
    if com == 0:
        print('초기화')
        board = deepcopy(default)
        com_q = []
    elif com == 1:
        print('상하반전')
        board.reverse()
    elif com == 2:
        print('좌우반전')
        for i in range(len(board)):
            board[i].reverse()
    elif com == 3:
        print('시계방향회전')
        new = list()
        for j in range(len(board[0])):
            new.append([board[i][j] for i in range(len(board)-1, -1, -1)])
        board = new
    elif com == 4:
        print('반시계방향회전')
        new = list()
        for j in range(len(board[0])-1, -1, -1):
            new.append([board[i][j] for i in range(len(board))])
        board = new
    elif com == 5:
        print('4등분해서 시계방향회전')
        n2 = len(board)//2
        m2 = len(board[0])//2
        for i in range(n2):
            for j in range(m2):
                board[i][j], board[i][j+m2], board[i+n2][j+m2], board[i + n2][j]\
                    = board[i+n2][j], board[i][j], board[i][j+m2], board[i+n2][j+m2]
    elif com == 6:
        print('4등분해서 반시계방향회전')
        n2 = len(board)//2
        m2 = len(board[0])//2
        for i in range(n2):
            for j in range(m2):
                board[i][j], board[i][j+m2], board[i+n2][j+m2], board[i + n2][j]\
                    = board[i][j+m2], board[i+n2][j+m2], board[i+n2][j], board[i][j]

print('end')
