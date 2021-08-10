def solution(N, road, K):
    answer = 0

    cost = [[-1 for j in range(N)] for i in range(N)]
    edge = [set() for i in range(N)]
    chk = [999999999 for i in range(N)]

    for r in road:
        a, b, c = r[0]-1, r[1]-1, r[2]
        # print(a, b, c)
        cost[a][b] = c
        cost[b][a] = c
        edge[a].add(b)
        edge[b].add(a)

    ans = {0}
    chk[0] = 0
    q = [0]
    while len(q) > 0:
        now = q.pop(0)
        for nxt in edge[now]:
            tmp = chk[now]+cost[now][nxt]
            if K > tmp and chk[nxt] > tmp:
                ans.add(nxt)
                q.append(nxt)
                chk[nxt] = tmp
            elif K == tmp and chk[nxt] > tmp:
                ans.add(nxt)
                chk[nxt] = tmp
    return len(ans)


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
                   [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
