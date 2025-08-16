import sys
import heapq

inputs = sys.stdin.readlines()
n = int(inputs[0])
m = int(inputs[1])
graph = dict()
for i in range(2, 2 + m):
    a, b, cost = map(int, inputs[i].split())
    graph.setdefault(a, dict())
    graph[a].setdefault(b, float("inf"))
    graph[a][b] = min(cost, graph[a][b])
start, dest = map(int, inputs[-1].split())

d = [float("inf") for _ in range(n + 1)]
route = [-1 for _ in range(n + 1)]
d[start] = 0
q = [(start, 0)]
while len(q) > 0:
    cur, cost = q.pop(0)
    if cur in graph:
        for nxt in graph[cur]:
            nxt_cost = cost + graph[cur][nxt]
            if nxt_cost < d[nxt]:
                d[nxt] = nxt_cost
                route[nxt] = cur
                q.append((nxt, nxt_cost))

ans_route = list()
cur = dest
while cur != -1:
    ans_route.append(str(cur))
    cur = route[cur]
ans_route.reverse()

print(d[dest])
print(len(ans_route))
print(" ".join(ans_route))
