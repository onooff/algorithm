def solution(a, edges):
    answer = 0
    test_sum = 0
    test_set = set()
    idx = 0
    d = dict()
    for aa in a:
        d.setdefault(idx, set())
        test_sum += aa
        test_set.add(aa)
        idx += 1
    if test_sum != 0:
        return -1
    if len(test_set) == 1:
        return 0

    for e in edges:
        d[e[0]].add(e[1])
        d[e[1]].add(e[0])

    go = list()
    for k in d:
        if len(d[k]) == 1:
            go.append(k)

    idx = 0
    while idx < len(go):
        tmp = go[idx]
        for parent in d[tmp]:
            answer += abs(a[tmp])
            a[parent] += a[tmp]

            d[parent].discard(tmp)
            if len(d[parent]) == 1:
                go.append(parent)
            # if a[tmp] != 0:
            #     test_set.discard(a[tmp])
            #     test_set.discard(a[parent])
            #     answer += abs(a[tmp])
            #     a[parent] += a[tmp]
            #     test_set.add(a[parent])
            #     if len(test_set) == 1:
            #         return answer
        # print(len(d[tmp]), len(test_set), test_set)
        idx += 1
        # print(idx, len(go))
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
