import sys
import itertools


def dijkstra(K, V, graph):
    INF = sys.maxsize
    s = [False] * V
    d = [INF] * V
    d[K - 1] = 0

    while True:
        m = INF
        N = -1

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
        if m == INF:
            break

        s[N] = True

        for j in range(V):
            if s[j]:
                continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via

    return d


n, k = map(int, input().split())
d_table = list()
for i in range(n):
    d_table.append(list(map(int, input().split())))

min_d = list()
for i in range(n):
    min_d.append(dijkstra(i, n, d_table))
# print(min_d)
min_d.append(min_d.pop(0))
print(min_d)


r = set(range(0, n))
r.remove(k)
p = itertools.permutations(r, n-1)
# print(list(p))

INF = sys.maxsize
ans = INF

for go in list(p):
    go = list(go)
    go.insert(0, k)
    # print(go)
    tmp = 0
    for i in range(len(go)-1):
        tmp += min_d[go[i]][go[i+1]]
    ans = min(ans, tmp)

print(ans)
