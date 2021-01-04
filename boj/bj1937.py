import heapq


def isIn(y, x, n):
    return y >= 0 and x >= 0 and y < n and x < n


n = int(input())
board = list()
dp = list()
hq = list()
for i in range(n):
    dp.append(list())
    board.append(list(map(int, input().split())))
    for j in range(n):
        dp[i].append(0)
        heapq.heappush(hq, (-board[i][j], (i, j)))
ans = -1
while len(hq) > 0:
    tmp = heapq.heappop(hq)
    ty = tmp[1][0]
    tx = tmp[1][1]
    dp[ty][tx] += 1
    ans = max(ans, dp[ty][tx])
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = ty+d[0]
        nx = tx+d[1]
        if isIn(ny, nx, n) and board[ny][nx] < board[ty][tx]:
            dp[ny][nx] = max(dp[ty][tx], dp[ny][nx])

print(ans)
