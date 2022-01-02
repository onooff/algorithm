import sys

lim = 31
dp = list()
for w in range(lim):
    dp.append(list())
    for h in range(w):
        if h == 0:
            dp[w].append(1)
        elif h == w-1:
            dp[w].append(dp[w][h-1]+dp[w-1][h-1])
        else:
            dp[w].append(dp[w][h-1]+dp[w-1][h])

inputs = sys.stdin.readlines()
for i in range(len(inputs)-1):
    n = int(inputs[i])
    print(dp[n][n-1])
