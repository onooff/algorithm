import sys

info = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()[1:]))
n = len(info)

ans = float("inf")
for start in range(3):
    dp = [[float("inf") for _ in range(3)] for _ in range(n)]
    dp[0][start] = info[0][start]
    for i in range(1, n):
        for j in range(3):
            if not (i == n - 1 and j == start):
                dp[i][j] = info[i][j] + min(
                    dp[i - 1][(j + 1) % 3], dp[i - 1][(3 + j - 1) % 3]
                )
    # print(dp)
    ans = min(ans, min(dp[-1]))
print(ans)
