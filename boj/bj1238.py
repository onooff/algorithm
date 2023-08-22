import sys
import heapq

INF = float("inf")
inputs = sys.stdin.readlines()

n, m, x = map(int, inputs[0].rstrip().split())
d = dict()
rd = dict()
for i in range(1, len(inputs)):
    a, b, c = map(int, inputs[i].rstrip().split())
    d.setdefault(a, dict())
    rd.setdefault(b, dict())
    d[a][b] = c
    rd[b][a] = c


x_to_home = [INF for _ in range(n + 1)]
x_to_home[x] = -1
q = [(x, 0)]
while q:
    cur, cost = heapq.heappop(q)
    for nxt in d[cur]:
        ncost = d[cur][nxt] + cost
        if ncost < x_to_home[nxt]:
            x_to_home[nxt] = ncost
            heapq.heappush(q, (nxt, ncost))

home_to_x = [INF for _ in range(n + 1)]
home_to_x[x] = -1
q = [(x, 0)]
while q:
    cur, cost = heapq.heappop(q)
    for nxt in rd[cur]:
        ncost = rd[cur][nxt] + cost
        if ncost < home_to_x[nxt]:
            home_to_x[nxt] = ncost
            heapq.heappush(q, (nxt, ncost))

ans = -1
for i in range(1, n + 1):
    if i == x:
        continue
    ans = max(ans, x_to_home[i] + home_to_x[i])
print(ans)
