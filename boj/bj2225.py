n, k = map(int, input().split())

dp = list()
dp.append(list())
for i in range(n+1):
    dp[0].append(1)

for i in range(1, k):
    dp.append(list())
    dp[i].append(1)
    for j in range(1, n+1):
        dp[i].append(dp[i][j-1]+dp[i-1][j])

print(dp[k-1][n] % 1000000000)

# for i in range(k+1):
#     print(dp[i])
