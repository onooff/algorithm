def solution(edges):
    g = dict()
    v = set()
    come = set()
    for e in edges:
        a, b = e[0], e[1]
        g.setdefault(a, set())
        g[a].add(b)
        v.add(a)
        v.add(b)
        come.add(b)

    start_candidate = v - come
    start = -1
    for s in start_candidate:
        if len(g[s]) > 1:
            start = s
            break

    answer = [start, 0, 0, 0]
    for v in g[start]:
        visitd = {v}
        cur = v
        while True:
            if cur not in g:
                answer[2] += 1
                break
            elif len(g[cur]) >= 2:
                answer[3] += 1
                break
            nxt = list(g[cur])[0]
            if nxt in visitd:
                answer[1] += 1
                break
            visitd.add(nxt)
            cur = nxt
    return answer
