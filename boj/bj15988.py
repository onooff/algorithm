d = 1000000009
lim = 1000000

dp = [0 for _ in range(lim + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, lim + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % d

tc = int(input())
for _ in range(tc):
    print(dp[int(input())])
