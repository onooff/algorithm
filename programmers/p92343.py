def solution(info, edges):
    answer = 0
    g = {x: set() for x in range(len(info))}
    for e in edges:
        g[e[0]].add(e[1])
    q = [(0,)]
    visited = {(0,)}
    while q:
        cur = q.pop()
        s, w = 0, 0
        nxts = list()
        chk = set(cur)
        for node in cur:
            if info[node] == 0:
                s += 1
            else:
                w += 1
            for nxt in g[node]:
                if nxt not in chk:
                    nxts.append(nxt)
        answer = max(answer, s)
        diff = s - w
        if diff == 1:
            for nxt in nxts:
                n = tuple(sorted(list(cur + (nxt,))))
                if info[nxt] == 0 and n not in visited:
                    q.append(n)
                    visited.add(n)
        else:
            for nxt in nxts:
                n = tuple(sorted(list(cur + (nxt,))))
                if n not in visited:
                    q.append(n)
                    visited.add(n)

    return answer


"""
#edge case
print(
    solution(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [
            [0, 1],
            [0, 2],
            [1, 3],
            [1, 4],
            [2, 5],
            [2, 6],
            [3, 7],
            [3, 8],
            [4, 9],
            [4, 10],
            [5, 11],
            [5, 12],
            [6, 13],
            [6, 14],
            [7, 15],
            [7, 16],
        ],
    )
)
"""
