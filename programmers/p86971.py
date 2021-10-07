def solution(n, wires):
    answer = 9999999999999999999999999
    graph = dict()
    for w in wires:
        graph.setdefault(w[0], set())
        graph.setdefault(w[1], set())
        graph[w[0]].add(w[1])
        graph[w[1]].add(w[0])

    for w in wires:
        graph[w[0]].discard(w[1])
        graph[w[1]].discard(w[0])

        q = [w[0]]
        chk_set = {w[0]}
        q_idx = 0
        while q_idx < len(q):
            cur = q[q_idx]
            q_idx += 1

            for nxt in graph[cur]:
                if nxt not in chk_set:
                    q.append(nxt)
                    chk_set.add(nxt)
        answer = min(answer, abs(len(q)-(n-len(q))))

        graph[w[0]].add(w[1])
        graph[w[1]].add(w[0])

    return answer
