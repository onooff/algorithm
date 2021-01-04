import sys
board = list()
need = list()
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            need.append((i, j))


def chk(y, x, num):
    global board
    for i in range(9):
        if board[y][i] == num or board[i][x] == num:
            return False
    for i in range((y//3)*3, (y//3)*3+3):
        for j in range((x//3)*3, (x//3)*3+3):
            if board[i][j] == num:
                return False
    return True


def dfs(idx=0):
    global need, board
    if idx == len(need):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        sys.exit()

    for i in range(1, 10):
        if chk(need[idx][0], need[idx][1], i):
            board[need[idx][0]][need[idx][1]] = i
            dfs(idx+1)
            board[need[idx][0]][need[idx][1]] = 0


dfs(0)
