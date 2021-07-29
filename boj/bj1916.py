'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
import heapq

inf = 999999999999999999
n = int(input())
graph = [list() for i in range(n)]
m = int(input())
for i in range(m):
    s, e, c = map(int, input().split())
    s -= 1
    e -= 1
    graph[s].append((e, c))
# for i in range(n):
#     graph[i].sort(key=lambda x: x[1])
# print(graph)

start, end = map(int, input().split())
start -= 1
end -= 1
cost = [inf for i in range(n)]

cost[start] = 0
q = [(cost[start], start)]
heapq.heapify(q)

while len(q) > 0:
    tmp = heapq.heappop(q)
    curr_town = tmp[1]
    curr_cost = tmp[0]
    if curr_cost>cost[end]:
        break
    for e in graph[curr_town]:
        # print(curr_cost, cost, e)
        if curr_cost+e[1] < cost[e[0]]:
            cost[e[0]] = curr_cost+e[1]
            # if e[0] == end:
            #     break
            heapq.heappush(q, (curr_cost+e[1], e[0]))

print(cost[end])
