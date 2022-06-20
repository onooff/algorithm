import copy
k, n, f = map(int, input().split())

graph = [{i} for i in range(n+1)]
for _ in range(f):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

ans = set()
for i in range(1, n+1):
    tmp = copy.deepcopy(graph[i])
    for friend in graph[i]:
        if friend not in tmp:
            continue
        tmp = tmp & graph[friend]
    # print(i, tmp)
    if len(tmp) >= k:
        ans = tmp
        break

if len(ans) == 0:
    print(-1)
else:
    ans = sorted(list(ans))
    for i in range(k):
        print(ans[i])
