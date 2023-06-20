input()
l = list(map(int, input().split()))
dp = [1 for i in range(len(l))]
ans = -1
for i in range(len(l)):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+1)
    if dp[i] > ans:
        ans = dp[i]
print(ans)
