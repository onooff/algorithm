import sys

l = list(map(int, sys.stdin.readlines()[1:]))
dp = [0 for i in range(len(l))]

for i in range(len(l)):
    a = l[i] + (l[i - 1] if i - 1 >= 0 else 0) + (dp[i - 3] if i - 3 >= 0 else 0)
    b = l[i] + (dp[i - 2] if i - 2 >= 0 else 0)
    c = dp[i - 1] if i - 1 >= 0 else 0
    dp[i] = max(a, b, c)
    # print(i, l[i], a, b, c, dp)
print(dp[-1])
