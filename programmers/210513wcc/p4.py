def solution(values, edges, queries):
    answer = []
    tree_c = dict()
    tree_p = dict()
    tree_sum = dict()
    for i in range(len(values)):
        tree_c.setdefault(i, set())
        tree_p.setdefault(i, -1)
        tree_sum.setdefault(i, values[i])
    for e in edges:
        tree_c[e[0]-1].add(e[1]-1)
        tree_c[e[1]-1].add(e[0]-1)
    bfs = list()
    nbfs = list()
    bfs.append((0, 0))
    while len(bfs) > 0:
        tmp = bfs.pop(0)
        for child in tree_c[tmp[0]]:
            tree_c[child].discard(tmp[0])
            tree_p[child] = tmp[0]
            bfs.append((child, tmp[1]+1))
            nbfs.append((child, tmp[1]+1))
    bfs = nbfs
    bfs.sort(key=lambda x: -x[1])
    while len(bfs) > 0:
        tmp = bfs.pop(0)
        tmp = tmp[0]
        if tree_p[tmp] != -1:
            tree_sum[tree_p[tmp]] += tree_sum[tmp]

    # print(tree_c)
    # print(tree_p)
    # print(tree_sum)

    for q in queries:
        if q[1] == -1:
            answer.append(tree_sum[q[0]-1])
        else:
            now = q[0]-1
            p = tree_p[now]
            tree_sum[now] -= values[now]
            values[now] = values[p]
            tree_sum[now] += values[now]
            now = p
            p = tree_p[now]
            while p != -1:
                tree_sum[now] = 0
                for c in tree_c[now]:
                    tree_sum[now] += tree_sum[c]
                values[now] = values[p]
                tree_sum[now] += values[now]
                now = p
                p = tree_p[now]
            tree_sum[now] = 0
            for c in tree_c[now]:
                tree_sum[now] += tree_sum[c]
            values[now] = q[1]
            tree_sum[now] += values[now]
            # print(q[1], now)
            # print('>>>', q)
            # print(values)
            # print(tree_sum)

    return answer


print(solution(	[1, 10, 100, 1000, 10000], [[1, 2], [1, 3], [2, 4], [2, 5]], [[1, -1], [2, -1], [3, -1], [4, -1],
                                                                              [5, -1], [4, 1000], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [2, 1], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]))
print([11111, 11010, 100, 1000, 10000, 11111, 10011,
       100, 10, 10000, 11111, 11010, 100, 10, 10000])
