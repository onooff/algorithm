# inf = 99999999999999999
# t = int(input())
# for tc in range(t):
#     n, m, w = map(int, input().split())
#     roads = dict()
#     worms = dict()
#     for i in range(1, n+1):
#         roads.setdefault(i, dict())
#     for i in range(m):
#         s, e, t = map(int, input().split())
#         if e not in roads[s]:
#             roads[s].setdefault(e, t)
#         else:
#             roads[s][e] = min(roads[s][e], t)
#         if s not in roads[e]:
#             roads[e].setdefault(s, t)
#         else:
#             roads[e][s] = min(roads[e][s], t)
#     for i in range(w):
#         s, e, t = map(int, input().split())
#         if e not in roads[s]:
#             roads[s].setdefault(e, -t)
#         else:
#             roads[s][e] = min(roads[s][e], -t)
#     is_ans = False
#     for i in range(1, m+1):
#         board = [inf for j in range(n+1)]
#         board[i] = 0
#         q = [i]
#         while len(q) > 0:
#             now = q.pop(0)
#             for go in roads[now]:
#                 if board[now]+roads[now][go] < board[go]:
#                     board[go] = board[now]+roads[now][go]
#                     if board[i] < 0:
#                         break
#                     q.append(go)
#         if board[i] < 0:
#             # print(i, board)
#             is_ans = True

#     for i in range(n):
#         for

#     if is_ans:
#         print("YES")
#     else:
#         print("NO")


inf = 99999999999999999
t = int(input())
for tc in range(t):
    n, m, w = map(int, input().split())
    edg = dict()
    for i in range(1, n+1):
        for j in range(1, n+1):
            edg.setdefault((i, j), inf)
    for i in range(m):
        s, e, t = map(int, input().split())
        edg[(s, e)] = min(edg[(s, e)], t)
        edg[(e, s)] = min(edg[(e, s)], t)
    for i in range(w):
        s, e, t = map(int, input().split())
        edg[(s, e)] = min(edg[(s, e)], -t)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if edg[(i, j)] == inf:
                edg.pop((i, j))

    is_ans = False
    # for start in range(1, n+1):
    d = [inf for i in range(n+1)]
    d[i] = 0
    for i in range(1, n+1):
        for e in edg:
            now = e[0]
            go = e[1]
            val = edg[e]
            if d[go] > d[now]+val:
                if i == n:
                    is_ans = True
                    break
                d[go] = d[now]+val
        if is_ans:
            break
        # print(d)
        # if d[start] < 0 or is_ans:
        #     is_ans = True
        #     break
    if is_ans:
        print("YES")
    else:
        print("NO")
