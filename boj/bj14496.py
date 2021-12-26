import sys

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())
graph = {i: set() for i in range(n + 1)}
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    graph[i].add(j)
    graph[j].add(i)
if a == b:
    print(0)
else:
    visit = [False for i in range(len(graph))]
    visit[a] = True
    q = [a]
    idx = 0
    ans = -1
    nq = list()
    d = 0
    while ans == -1 and idx < len(q):
        cur = q[idx]
        idx += 1
        for nxt in graph[cur]:
            if nxt == b:
                ans = d + 1
                break
            if not visit[nxt]:
                visit[nxt] = True
                nq.append(nxt)
        if idx == len(q) and len(nq) > 0:
            q = nq
            nq = list()
            idx = 0
            d += 1
    print(ans)
