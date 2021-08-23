import heapq
import copy


def solution(n, s, a, b, fares):
    answer = 0
    graph = dict()
    for i in range(1, n+1):
        graph.setdefault(i, {i: 0})

    for f in fares:
        graph[f[0]].setdefault(f[1], f[2])
        graph[f[1]].setdefault(f[0], f[2])

    inf = 999999999999999999
    ab = [-1]
    s_cost = list()
    for i in range(1, n+1):
        cost = [inf for i in range(n+1)]
        cost[i] = 0
        q = [(0, i)]
        while len(q) > 0:
            tmp = heapq.heappop(q)
            for nxt in graph[tmp[1]]:
                if cost[nxt] > tmp[0]+graph[tmp[1]][nxt]:
                    cost[nxt] = tmp[0]+graph[tmp[1]][nxt]
                    heapq.heappush(q, (cost[nxt], nxt))
        ab.append(cost[a]+cost[b])
        if i == s:
            s_cost = copy.deepcopy(cost)

    ans = inf
    for i in range(1, n+1):
        if s_cost[i]+ab[i] < ans:
            ans = s_cost[i]+ab[i]
    return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

print(solution(	7, 3, 4, 1, [[5, 7, 9], [
      4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

print(solution(	6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [
      6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
