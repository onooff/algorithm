import sys

readline = sys.stdin.readline
n, m = map(int, readline().split())
board = [list(map(int, readline().split())) for _ in range(n)]
summ = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp = board[i][j]
        if i - 1 >= 0:
            tmp += summ[i - 1][j]
        if j - 1 >= 0:
            tmp += summ[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            tmp -= summ[i - 1][j - 1]
        summ[i][j] = tmp
# list(map(print, summ))
for i in range(m):
    sy, sx, ey, ex = map(lambda x: int(x) - 1, readline().split())
    ans = summ[ey][ex]
    if sy - 1 >= 0:
        ans -= summ[sy - 1][ex]
    if sx - 1 >= 0:
        ans -= summ[ey][sx - 1]
    if sy - 1 >= 0 and sx - 1 >= 0:
        ans += summ[sy - 1][sx - 1]
    print(ans)
