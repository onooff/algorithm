import sys

dp = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1],
]
while len(dp) < 10001:
    dp.append([1, dp[-2][0] + dp[-2][1], sum(dp[-3])])

inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    print(sum(dp[int(inputs[i])]))
