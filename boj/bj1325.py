import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())

graph = [[] for i in range(n + 1)]

for i in range(1, len(inputs)):
    a, b = map(int, inputs[i].split())
    graph[b].append(a)

maxx = -1
ans = []
for i in range(1, n + 1):
    cur_visited = [False] * (n + 1)
    cur_visited[i] = True
    q = [i]
    idx = 0
    while idx < len(q):
        cur = q[idx]
        for nxt in graph[cur]:
            if cur_visited[nxt] == False:
                cur_visited[nxt] = True
                q.append(nxt)
        idx += 1
    if maxx < len(q):
        maxx = len(q)
        ans = []
    if maxx == len(q):
        ans.append(i)

print(" ".join(map(str, ans)))
