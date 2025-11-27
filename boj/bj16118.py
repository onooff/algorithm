import sys
import heapq
from collections import defaultdict

inf = float("inf")
inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].split())

graph = [[] for i in range(n + 1)]
for i in range(1, len(inputs)):
    a, b, d = map(int, inputs[i].split())
    graph[a].append((b, d))
    graph[b].append((a, d))

shortest_fox = [inf for _ in range(n + 1)]
shortest_fox[1] = 0
q = list()
heapq.heappush(q, (0, 1))
while len(q) > 0:
    cur_d, cur = heapq.heappop(q)
    if cur_d > shortest_fox[cur]:
        continue
    for nxt, nxt_d in graph[cur]:
        nd = cur_d + (nxt_d * 2)
        if shortest_fox[nxt] > nd:
            shortest_fox[nxt] = nd
            heapq.heappush(q, (nd, nxt))

shortest_wolf = [[inf for _ in range(n + 1)] for i in range(2)]
shortest_wolf[1][1] = 0
q = list()
heapq.heappush(q, (0, 1, True))
while len(q) > 0:
    cur_d, cur, wolf_flag = heapq.heappop(q)
    if cur_d > shortest_wolf[wolf_flag][cur]:
        continue
    wolf_flag = not wolf_flag
    for nxt, nxt_d in graph[cur]:
        if wolf_flag == True:
            nd = cur_d + (nxt_d * 4)
        else:
            nd = cur_d + nxt_d
        if shortest_wolf[wolf_flag][nxt] > nd:
            shortest_wolf[wolf_flag][nxt] = nd
            heapq.heappush(q, (nd, nxt, wolf_flag))
# print(shortest_fox)
# print(shortest_wolf)

ans = 0
for i in range(n + 1):
    if (shortest_fox[i] < shortest_wolf[0][i]) and (
        shortest_fox[i] < shortest_wolf[1][i]
    ):
        ans += 1
print(ans)
