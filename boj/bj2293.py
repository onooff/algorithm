import sys

input = sys.stdin.readline
n, k = map(int, input().split())

l = list()
for _ in range(n):
    l.append(int(input()))
l.sort()

dp = [0 for _ in range(k + 1)]
dp[0] = 1
for num in l:
    for i in range(num, len(dp)):
        if i - num < 0:
            break
        dp[i] += dp[i - num]

print(dp[k])
