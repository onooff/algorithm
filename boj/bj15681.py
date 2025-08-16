import sys

inputs = sys.stdin.readlines()

n, r, query = map(int, inputs[0].split())
graph = dict()
for i in range(1, n):
    a, b = map(int, inputs[i].split())
    graph.setdefault(a, set())
    graph.setdefault(b, set())
    graph[a].add(b)
    graph[b].add(a)

parent = [-1 for _ in range(n + 1)]
parent[r] = 0
q = [r]
nq = list()
while len(q) > 0:
    cur = q.pop(0)
    is_leaf = True
    if cur in graph:
        for nxt in list(graph[cur]):
            if parent[nxt] == -1:
                parent[nxt] = cur
                q.append(nxt)
                is_leaf = False
            else:
                graph[cur].discard(nxt)
    if is_leaf:
        nq.append(cur)

childs_cnt = [1 for _ in range(n + 1)]
q = nq
while len(q) > 0:
    cur = q.pop(0)
    childs_cnt[parent[cur]] += childs_cnt[cur]
    if parent[cur] != 0:
        graph[parent[cur]].discard(cur)
        if len(graph[parent[cur]]) == 0:
            q.append(parent[cur])

for i in range(n, len(inputs)):
    print(childs_cnt[int(inputs[i])])
