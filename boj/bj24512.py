def dfs(route, chk, graph, maxx):
    if len(route) == len(graph):
        if route[0] in graph[route[-1]] and graph[route[-1]][route[0]] <= maxx:
            return True
        return False

    cur = route[-1]
    for nxt in graph[cur]:
        if nxt not in chk and graph[cur][nxt] <= maxx:
            route.append(nxt)
            chk.add(nxt)
            ret = dfs(route, chk, graph, maxx)
            if ret:
                return ret
            chk.discard(nxt)
            route.pop()


n, m = map(int, input().split())
graph = {i+1: dict() for i in range(n)}
edges = list()
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    graph[a].setdefault(b, c)

edges.sort(key=lambda x: -x[2])

is_ans = False
maxx_edge = -1
ans_route = None
for e in edges:
    if e[2] == maxx_edge:
        continue
    route = [e[0], e[1]]
    chk = set(route)
    is_ans = dfs(route, chk, graph, e[2])
    if is_ans:
        maxx_edge = e[2]
        ans_route = ' '.join(list(map(str, route)))

print(maxx_edge)
if maxx_edge > 0:
    print(ans_route)
