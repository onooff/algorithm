import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[n - 1][m - 1] = 1

d = ((0, -1), (0, 1), (-1, 0), (1, 0))


def dfs(y, x):
    global n, m
    if y == n - 1 and x == m - 1:
        return dp[y][x]

    if dp[y][x] == -1:
        dp[y][x] = 0

    for nd in d:
        ny = y + nd[0]
        nx = x + nd[1]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] < board[y][x]:
            if dp[ny][nx] == -1:
                dp[y][x] += dfs(ny, nx)
            else:
                dp[y][x] += dp[ny][nx]

    return dp[y][x]


dfs(0, 0)

print(dp[0][0])
