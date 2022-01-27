import sys
inputs = sys.stdin.readlines()
n, r = map(int, inputs[0].split())
r -= 1
g = {i: dict() for i in range(n)}
for i in range(1, len(inputs)):
    a, b, d = map(int, inputs[i].split())
    a, b, = a-1, b-1
    g[a].setdefault(b, d)
    g[b].setdefault(a, d)

q = [(r, 0)]
idx = 0

ans1 = -1
ans2 = 0

while idx < len(q):
    cur = q[idx]
    idx += 1
    node = cur[0]
    c = cur[1]
    ans2 = max(ans2, c)
    if ans1 < 0 and len(g[node]) >= 2:
        ans1 = c
    for nxt in g[node]:
        g[nxt].pop(node)
        q.append((nxt, c+g[node][nxt]))

if ans1 == -1:
    ans1 = ans2
print(ans1, ans2-ans1)
