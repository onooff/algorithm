import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

ans = -1
for d in range(-99, 100):
    dp = [0 for i in range(101)]
    for num in l:
        if 0 <= num-d <= 100:
            dp[num] = dp[num-d]+1
        else:
            dp[num] = 1
        ans = max(ans, dp[num])
print(ans)
