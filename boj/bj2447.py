n = int(input())
board = [[' ' for _ in range(n)] for _ in range(n)]


def dfs(board, y, x, n):
    # print(n)
    if n == 1:
        board[y][x] = '*'
        return

    d = n//3
    for i in range(y, y+n, d):
        for j in range(x, x+n, d):
            if i == y+d and j == x+d:
                continue
            dfs(board, i, j, d)


dfs(board, 0, 0, n)
for i in range(n):
    print(''.join(board[i]))
