dp = [1]*(10**6+1)
n = 3
c = n
for i in range(2, len(dp)):
    c -= 1
    if c == n-2:
        dp[i] = n-1
    else:
        dp[i] = n
    if c == 0:
        n += 1
        c = n

t = int(input())

for tc in range(t):
    n = int(input())
    print(dp[n])
