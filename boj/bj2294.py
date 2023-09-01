import sys

inputs = sys.stdin.readlines()
n, k = map(int, inputs[0].rstrip().split())
coins = sorted(list(set(map(int, inputs[1:]))))

dp = [float("inf") for _ in range(k + 1)]
dp[0] = 0
for c in coins:
    for i in range(len(dp) - c):
        dp[i + c] = min(dp[i + c], dp[i] + 1)

if dp[-1] == float("inf"):
    dp[-1] = -1
print(dp[-1])
