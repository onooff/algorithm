import sys


def solve():
    board = list(map(lambda x: list(x.rstrip()), sys.stdin.readlines()[1:]))
    n = len(board)
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))

    maxx = -1
    for i in range(n):
        for j in range(n):
            for nd in d:
                ny = i + nd[0]
                nx = j + nd[1]
                if 0 <= ny < n and 0 <= nx < n:
                    board[i][j], board[ny][nx] = board[ny][nx], board[i][j]
                    cur = board[i][j]

                    cnt = 1
                    for k in range(j - 1, -1, -1):
                        if board[i][k] != cur:
                            break
                        cnt += 1
                    for k in range(j + 1, n):
                        if board[i][k] != cur:
                            break
                        cnt += 1
                    if cnt > maxx:
                        maxx = cnt

                    cnt = 1
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != cur:
                            break
                        cnt += 1
                    for k in range(i + 1, n):
                        if board[k][j] != cur:
                            break
                        cnt += 1
                    if cnt > maxx:
                        maxx = cnt

                    board[i][j], board[ny][nx] = board[ny][nx], board[i][j]
                    if maxx >= n:
                        return maxx
    return maxx


print(solve())
