import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
board = [list(map(int, inputs[i].split())) for i in range(1, n + 1)]

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
# 0가로 1대각 2세로
dp[0][0][1] = 1


def is_ok(y, x, n):
    return (0 <= y < n) and (0 <= x < n)


i = 0
for y in range(n):
    for x in range(n):
        for status in range(3):
            if status == 0:  # 현재 가로, 다음 가로 or 대각
                ny = y
                nx = x + 1
                if is_ok(ny, nx, n) and board[ny][nx] == 0:
                    dp[0][ny][nx] += dp[status][y][x]
                ny = y + 1
                nx = x + 1
                if (
                    is_ok(ny, nx, n)
                    and board[ny][x] == 0
                    and board[ny][nx] == 0
                    and board[y][nx] == 0
                ):
                    dp[1][ny][nx] += dp[status][y][x]
            elif status == 1:  # 현재 대각, 다음 가로 or 대각 or 세로
                ny = y
                nx = x + 1
                if is_ok(ny, nx, n) and board[ny][nx] == 0:
                    dp[0][ny][nx] += dp[status][y][x]
                ny = y + 1
                nx = x + 1
                if (
                    is_ok(ny, nx, n)
                    and board[ny][x] == 0
                    and board[ny][nx] == 0
                    and board[y][nx] == 0
                ):
                    dp[1][ny][nx] += dp[status][y][x]
                ny = y + 1
                nx = x
                if is_ok(ny, nx, n) and board[ny][nx] == 0:
                    dp[2][ny][nx] += dp[status][y][x]
            else:  # status==2: # 현재 세로, 다음 대각 or 세로
                ny = y + 1
                nx = x + 1
                if (
                    is_ok(ny, nx, n)
                    and board[ny][x] == 0
                    and board[ny][nx] == 0
                    and board[y][nx] == 0
                ):
                    dp[1][ny][nx] += dp[status][y][x]
                ny = y + 1
                nx = x
                if is_ok(ny, nx, n) and board[ny][nx] == 0:
                    dp[2][ny][nx] += dp[status][y][x]
print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])

# list(map(print, dp[0]))
# print('--------------------')
# list(map(print, dp[1]))
# print('--------------------')
# list(map(print, dp[2]))
