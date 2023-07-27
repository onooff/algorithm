import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
l = [list(map(int, inputs[x].split())) for x in range(1, len(inputs))]

dp = [
    [
        float("inf") if j == 0 else l[0][j],
        l[0][j],
        float("inf") if j == m - 1 else l[0][j],
    ]
    for j in range(m)
]

for i in range(1, n):
    nxt = list()
    for j in range(m):
        nxt.append(
            [
                float("inf") if j == 0 else min(dp[j - 1][1], dp[j - 1][2]) + l[i][j],
                min(dp[j][0], dp[j][2]) + l[i][j],
                float("inf")
                if j == m - 1
                else min(dp[j + 1][0], dp[j + 1][1]) + l[i][j],
            ]
        )
    dp = nxt

minn = float("inf")
for d in dp:
    minn = min(minn, min(d))
print(minn)
