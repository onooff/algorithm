import sys

inputs = sys.stdin.readlines()
tree = dict()
parent = dict()
for line in inputs[1:]:
    line = list(map(int, line.split()))
    cur = line[0]
    i = 1
    while line[i] != -1:
        nxt = line[i]
        cost = line[i + 1]
        tree.setdefault(cur, dict())
        tree[cur][nxt] = cost
        parent[nxt] = cur
        i += 2

q = [(1, 0)]
visited = {1}
maxx = (-1, -1)
while len(q) > 0:
    cur = q.pop(0)
    if maxx[1] < cur[1]:
        maxx = cur
    if cur[0] in tree:
        for nxt in tree[cur[0]].keys():
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cur[1] + tree[cur[0]][nxt]))
    if cur[0] in parent and parent[cur[0]] not in visited:
        visited.add(parent[cur[0]])
        q.append((parent[cur[0]], cur[1] + tree[parent[cur[0]]][cur[0]]))

q = [(maxx[0], 0)]
visited = {maxx[0]}
maxx = (-1, -1)
while len(q) > 0:
    cur = q.pop(0)
    if maxx[1] < cur[1]:
        maxx = cur
    if cur[0] in tree:
        for nxt in tree[cur[0]].keys():
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cur[1] + tree[cur[0]][nxt]))
    if cur[0] in parent and parent[cur[0]] not in visited:
        visited.add(parent[cur[0]])
        q.append((parent[cur[0]], cur[1] + tree[parent[cur[0]]][cur[0]]))

print(maxx[1])
