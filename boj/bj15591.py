'''
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1
'''

vn, qn = map(int, input().split())

# graph = [[0 for i in range(vn)] for j in range(vn)]
graph = dict()
for i in range(vn):
    graph.setdefault(i, list())

for i in range(vn-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # graph[a][b] = c
    # graph[b][a] = c
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(qn):
    k, start = map(int, input().split())
    start -= 1
    chk = [False for i in range(vn)]
    q = [start]
    chk[start] = True
    cnt = 0
    while len(q) > 0:
        now = q.pop(0)
        for nxt in graph[now]:
            if not chk[nxt[0]] and nxt[1] >= k:
                cnt += 1
                q.append(nxt[0])
                chk[nxt[0]] = True
    print(cnt)
