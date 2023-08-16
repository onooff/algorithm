import sys

input = sys.stdin.readline

t = int(input())
k = int(input())
l = list()
for i in range(k):
    l.append(tuple(map(int, input().rstrip().split())))
l.sort(key=lambda x: -x[0])

dp = [0 for i in range(t + 1)]
dp[0] = 1
visited = {0}

for coin_info in l:
    p = coin_info[0]
    n = coin_info[1]
    ndp = dp[::]
    for i in sorted(list(visited)):
        for j in range(1, n + 1):
            nxt = i + (p * j)
            if nxt > t:
                break
            ndp[nxt] += dp[i]
            visited.add(nxt)
    dp = ndp

print(dp[t])
