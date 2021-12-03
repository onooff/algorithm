'''
3 3 n,m 방개수,설치할수있는워프수
1 2 2 a-b 이동 비용
2 3 2
3 1 2
3 3 3 바로 탈출하는 비용
'''

import sys
sys.setrecursionlimit(200000)
inf = 999999999
inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].rstrip().split())
graph = dict()

for i in range(1, m+1):
    a, b, c = map(int, inputs[i].rstrip().split())
    if not(a in graph and b in graph and b in graph[a] and a in graph[b]):
        graph.setdefault(a, dict())
        graph[a].setdefault(b, c)
        graph.setdefault(b, dict())
        graph[b].setdefault(a, c)
    elif graph[a][b] > c:
        graph[a][b] = c
        graph[b][a] = c

esc = inputs[m+1].rstrip().split()
for i in range(1, n+1):
    graph.setdefault(i, dict())
    graph[i].setdefault(n+1, int(esc[i-1]))

edges = dict()
for a in graph:
    for b in graph[a]:
        if a < b:
            edges.setdefault(graph[a][b], set())
            edges[graph[a][b]].add((a, b))

# for k in graph:
#     print(k, graph[k])
# for k in edges:
#     print(k, edges[k])


def find(p, child):
    if p[child] == child:
        return child
    p[child] = find(p, p[child])
    return p[child]


'''
static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            p[y] = x;
        }
    }
'''


ans = 0
costs = list(edges.keys())
costs.sort()
p = {i: i for i in range(1, n+2)}
connect = n
for cost in costs:
    for edge in edges[cost]:
        a, b = edge
        pa = find(p, a)
        pb = find(p, b)
        if pa != pb:
            ans += cost
            p[pb] = p[pa]
            connect -= 1
        if connect <= 0:
            break
    if connect <= 0:
        break

# print(p)
print(ans)
