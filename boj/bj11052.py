n = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
dp = l[::]

for i in range(len(l) - 1, 0, -1):
    for k in range(1, i + 1):
        if i + k > len(l):
            break
        for j in range(i + k, len(l), i):
            dp[j] = max(dp[j], dp[j - i] + l[i])

print(dp[-1])
