import sys

inputs = sys.stdin.readlines()
board = list(map(lambda x: list(map(int, x.rstrip().split())), inputs[:-1]))
r, c = map(int, inputs[-1].split())
board[r][c] = -1

d = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(y, x, cnt, ate):
    if board[y][x] == 1:
        ate += 1

    if ate >= 2:
        return 1
    if cnt >= 3:
        return 0

    for nd in d:
        ny = y + nd[0]
        nx = x + nd[1]
        if 0 <= ny < 5 and 0 <= nx < 5 and board[ny][nx] != -1:
            tmp, board[ny][nx] = board[ny][nx], -1
            if dfs(ny, nx, cnt + 1, ate + tmp):
                return 1
            board[ny][nx] = tmp

    return 0


print(dfs(r, c, 0, 0))
