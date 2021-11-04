def solution(n, edge):
    graph = {i: set() for i in range(1, n+1)}
    chk = [False for i in range(n+1)]

    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    q = [1]
    chk[1] = True
    idx = 0
    cnt = 1
    n_cnt = 0
    last = 1
    while idx < len(q):
        cur = q[idx]
        idx += 1
        cnt -= 1
        for nxt in graph[cur]:
            if not chk[nxt]:
                q.append(nxt)
                chk[nxt] = True
                n_cnt += 1
        if cnt == 0 and idx < len(q):
            cnt = n_cnt
            last = n_cnt
            n_cnt = 0
    return last


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
