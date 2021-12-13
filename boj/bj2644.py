import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
graph = {i: set() for i in range(1, n + 1)}
d = [-1 for _ in range(n + 1)]
for i in range(3, len(inputs)):
    a, b = map(int, inputs[i].rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

chk = {i for i in range(1, n + 1)}
s, e = map(int, inputs[1].rstrip().split())
q = [s]
d[s] = 0
chk.discard(s)
idx = 0
while idx < len(q) and d[e] == -1:
    cur = q[idx]
    idx += 1
    for nxt in graph[cur]:
        if nxt in chk:
            q.append(nxt)
            d[nxt] = d[cur] + 1
            chk.discard(nxt)
print(d[e])
