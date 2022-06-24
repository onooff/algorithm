from math import inf
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

stations = dict()
routes = dict()
graph = dict()
transfers = set()
for i in range(N):
    tmp = input().split()[1:]
    routes[i] = {tmp[i]: i for i in range(len(tmp))}
    last = len(tmp)-1
    for j in range(len(tmp)):
        station = tmp[j]
        if station in stations:
            transfers.add(station)
        else:
            stations.setdefault(station, set())
        stations[station].add(i)
        graph.setdefault(station, set())
        if j != 0:
            graph[station].add(tmp[j-1])
        if j != last:
            graph[station].add(tmp[j+1])

routes_transfers = dict()
for k in routes:
    routes_transfers[k] = routes[k].keys() & transfers

d = dict()
for transfer in transfers:
    d[transfer] = {transfer: 0}
    q = [transfer]
    nq = list()
    idx = 0
    while idx < len(q):
        cur = q[idx]
        idx += 1
        for nxt in graph[cur]:
            if nxt not in d[transfer] or d[transfer][nxt] > d[transfer][cur]+1:
                d[transfer][nxt] = d[transfer][cur]+1
                nq.append(nxt)

        if idx >= len(q):
            q = nq
            nq = list()
            idx = 0

for _ in range(Q):
    a, b = input().split()
    ans = inf
    for route in stations[a]:
        if b in routes[route]:
            ans = min(ans, abs(routes[route][a]-routes[route][b]))
        for tranfer in routes_transfers[route]:
            if a in d[tranfer] and b in d[tranfer]:
                ans = min(ans, d[tranfer][a]+d[tranfer][b])
    if ans == inf:
        print(-1)
    else:
        print(ans*2)
