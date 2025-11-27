import sys

input = sys.stdin.readline
inf = float("inf")

tc = int(input())
for _ in range(tc):
    n, d, c = map(int, input().split())
    g = {i: dict() for i in range(n + 1)}
    for _ in range(d):
        a, b, s = map(int, input().split())
        g[b][a] = s
    di = [inf for i in range(n + 1)]
    di[c] = 0
    cur = c
    not_visited = {i for i in range(n)}
    for _ in range(n + 1):
        not_visited.discard(cur)
        for nxt in g[cur]:
            if di[nxt] >= di[cur] + g[cur][nxt]:
                di[nxt] = di[cur] + g[cur][nxt]
        minn = inf
        for nxt in not_visited:
            if di[nxt] < minn:
                minn = di[nxt]
                cur = nxt
        if minn == inf:
            break
    ans = [n for n in di if n != inf]
    print(len(ans), max(ans))
