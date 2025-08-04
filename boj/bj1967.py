import sys

inputs = sys.stdin.readlines()

tree = dict()
parent = dict()
for node_info in inputs[1:]:
    node_num, child_num, d = map(int, node_info.split())
    tree.setdefault(node_num, dict())
    tree[node_num].setdefault(child_num, d)
    parent[child_num] = node_num

q = [(1, 0)]
maxx = (-1, -1)
while len(q) > 0:
    cur = q.pop(0)
    if maxx[1] < cur[1]:
        maxx = cur
    if cur[0] in tree:
        for nxt in tree[cur[0]].keys():
            q.append((nxt, cur[1] + tree[cur[0]][nxt]))

# print(maxx)

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
