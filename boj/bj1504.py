'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
'''

import math

import sys
inputs = sys.stdin.readlines()
n, e = map(int, inputs[0].rstrip().split())
graph = {i: dict() for i in range(1, n+1)}
for i in range(1, e+1):
    a, b, c = map(int, inputs[i].rstrip().split())
    graph[a].setdefault(b, float(c))
    graph[b].setdefault(a, float(c))
v1, v2 = map(int, inputs[e+1].rstrip().split())

start_d = {i: math.inf for i in range(1, n+1)}
v1_d = {i: math.inf for i in range(1, n+1)}
v2_d = {i: math.inf for i in range(1, n+1)}

d = {1: start_d, v1: v1_d, v2: v2_d}

for go in d.keys():
    d[go][go] = 0
    q = [(go, 0)]
    q_idx = 0
    while q_idx < len(q):
        # print(q)
        cur = q[q_idx][0]
        cost = q[q_idx][1]
        q_idx += 1
        for nxt in graph[cur]:
            tmp = cost+graph[cur][nxt]
            if tmp < d[go][nxt]:
                d[go][nxt] = tmp
                q.append((nxt, tmp))
a = d[1][v1]+d[v1][v2]+d[v2][n]
b = d[1][v2]+d[v2][v1]+d[v1][n]
# print(a, b)
# print(d)
if a != math.inf or b != math.inf:
    print(int(min(a, b)))
else:
    print(-1)
