def solution(n, edge):
    answer = 0

    chk = [False]*(n+1)
    graph = dict()
    graphD = dict()
    for i in range(1, n+1):
        graph[i] = set()
        graphD[i] = 0

    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])

    q = list()
    chk[1] = True
    q.append([1, 0])
    maxD = 0

    while q:
        tmp = q.pop(0)

        for next in graph[tmp[0]]:
            if chk[next] == False:
                chk[next] = True
                q.append([next, tmp[1]+1])
                graphD[next] = tmp[1]+1
                maxD = max(maxD, tmp[1]+1)

    for i in graphD:
        if graphD[i] == maxD:
            answer += 1

    # print(graph)

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
