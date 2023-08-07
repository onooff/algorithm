import sys
import heapq

inputs = sys.stdin.readlines()

n, d = map(int, inputs[0].split())
g = dict()
v = {0, d}
for i in range(1, len(inputs)):
    a, b, cost = map(int, inputs[i].split())
    if b - a <= cost or a > d or b > d:
        continue
    g.setdefault(a, dict())
    g[a].setdefault(b, float("inf"))
    if g[a][b] > cost:
        g[a][b] = cost
    v.add(a)
    v.add(b)

v = sorted(list(v))
for i in range(1, len(v)):
    a = v[i - 1]
    b = v[i]
    cost = v[i] - v[i - 1]
    g.setdefault(a, dict())
    g[a].setdefault(b, float("inf"))
    if g[a][b] > cost:
        g[a][b] = cost

g.setdefault(d, dict())


dis = {x: float("inf") for x in v}
dis[0] = 0
q = [(0, 0)]

while len(q) > 0:
    tmp = heapq.heappop(q)
    cost = tmp[0]
    cur = tmp[1]

    for nxt in g[cur]:
        ncost = cost + g[cur][nxt]
        if dis[nxt] > ncost:
            dis[nxt] = ncost
            heapq.heappush(q, (ncost, nxt))

print(dis[d])
