n = int(input())
graph = [set() for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)

ans = [-1 for i in range(n)]

for i in range(n):
    is_cycle = False
    for go in graph[i]:
        chk = [False for i in range(n)]
        chk[go] = True
        graph[go].discard(i)

        q = [go]
        while len(q) > 0:
            now = q.pop(0)
            for nxt in graph[now]:
                if nxt == i:
                    is_cycle = True
                    q = []
                    break
                if not chk[nxt]:
                    chk[nxt] = True
                    q.append(nxt)

        if is_cycle:
            ans[i] = 0
        graph[go].add(i)
        if ans[i] != -1:
            break

for i in range(n):
    if ans[i] == 0 and len(graph[i]) > 2:
        q = [(i, 0)]
        while len(q) > 0:
            tmp = q.pop(0)
            now = tmp[0]
            d = tmp[1]+1
            for nxt in graph[now]:
                if ans[nxt] == -1:
                    ans[nxt] = d
                    q.append((nxt, d))

# print(ans)

for i in range(n):
    print(ans[i], end=' ')
print()
