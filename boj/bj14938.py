import sys

INF = float("inf")

inputs = sys.stdin.readlines()
n, m, r = map(int, inputs[0].split())
t = list(map(int, inputs[1].split()))
t.insert(0, 0)
graph = [[(0 if i == j else INF) for j in range(n + 1)] for i in range(n + 1)]
for i in range(r):
    a, b, d = map(int, inputs[i + 2].split())
    graph[a][b] = d
    graph[b][a] = d

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            graph[a][c] = min(graph[a][c], graph[a][b] + graph[b][c])
            graph[c][a] = graph[a][c]

maxx = -1
for start in range(1, n + 1):
    cur_maxx = 0
    for dest in range(1, n + 1):
        if graph[start][dest] <= m:
            cur_maxx += t[dest]
    maxx = max(maxx, cur_maxx)

print(maxx)
