import sys
import heapq

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())
d = dict()
for i in range(1, len(inputs)):
    a, b, cost = map(int, inputs[i].split())
    d.setdefault(a, dict())
    d[a].setdefault(b, float("inf"))
    d.setdefault(b, dict())
    d[b].setdefault(a, float("inf"))
    d[a][b] = min(d[a][b], cost)
    d[b][a] = min(d[b][a], cost)

ans = [float("inf") for _ in range(n + 1)]
ans[1] = 0
q = [(0, 1)]
while len(q) > 0:
    data = heapq.heappop(q)
    dis = data[0]
    node = data[1]
    if dis > ans[node]:
        continue

    for nxt in d[node]:
        if ans[nxt] > ans[node] + d[node][nxt]:
            ans[nxt] = ans[node] + d[node][nxt]
            heapq.heappush(q, (ans[nxt], nxt))

print(ans[n])
