input()
l = list(map(int, input().split()))
dp = [1 for i in range(len(l))]
rl = list(reversed(l))
rdp = [1 for i in range(len(l))]
for i in range(len(l)):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if rl[i] > rl[j]:
            rdp[i] = max(rdp[i], rdp[j] + 1)
rdp = list(reversed(rdp))

ans = -1
for i in range(len(l)):
    ans = max(ans, dp[i] + rdp[i] - 1)
print(ans)
