import sys
import heapq

inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].split())
d = dict()
for i in range(1, len(inputs)):
    a, b = map(int, inputs[i].split())
    d.setdefault(a, set())
    d[a].add(b)

l = [0 for _ in range(n + 1)]
l[1] = 100
q = [1]
while q:
    cur = heapq.heappop(q)
    if l[cur] == 0:
        continue
    if cur in d:
        w = l[cur] / len(d[cur])
        l[cur] = 0
        for nxt in d[cur]:
            l[nxt] += w
            heapq.heappush(q, nxt)

print(max(l))
