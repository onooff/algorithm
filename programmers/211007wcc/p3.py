# 2.9점
# def solution(n, m, x, y, queries):
#     d = ((0, -1), (0, 1), (-1, 0), (1, 0))
#     answer = 0
#     for i in range(n):
#         for j in range(m):
#             ni = i
#             nj = j
#             for q in queries:
#                 ni += d[q[0]][0]*q[1]
#                 nj += d[q[0]][1]*q[1]

#                 ni = min(ni, n-1)
#                 ni = max(ni, 0)

#                 nj = min(nj, m-1)
#                 nj = max(nj, 0)
#             # print((ni, nj))
#             if ni == x and nj == y:
#                 answer += 1
#     return answer

# 11.8점
# def solution(n, m, x, y, queries):
#     board = [[1 for _ in range(m)] for _ in range(n)]
#     for q in queries:
#         if q[0] == 0:
#             for _ in range(q[1]):
#                 for i in range(n):
#                     tmp = board[i].pop(0)
#                     board[i].append(0)
#                     board[i][0] += tmp
#         if q[0] == 1:
#             for _ in range(q[1]):
#                 for i in range(n):
#                     tmp = board[i].pop()
#                     board[i].insert(0, 0)
#                     board[i][m-1] += tmp
#         if q[0] == 2:
#             for _ in range(q[1]):
#                 tmp = board.pop(0)
#                 board.append([0 for _ in range(m)])
#                 for j in range(m):
#                     board[0][j] += tmp[j]
#         if q[0] == 3:
#             for _ in range(q[1]):
#                 tmp = board.pop()
#                 board.insert(0, [0 for _ in range(m)])
#                 for j in range(m):
#                     board[n-1][j] += tmp[j]
#     return board[x][y]

def solution(n, m, y, x, queries):
    inf = 99999999999999999999999999999
    nn = [inf, -inf]
    mm = [inf, -inf]
    dy = 0
    dx = 0
    for q in queries:
        if q[0] == 0:  # 열감소
            dx -= q[1]
        elif q[0] == 1:
            dx += q[1]
        elif q[0] == 2:  # 행감소
            dy -= q[1]
        elif q[0] == 3:
            dy += q[1]
        mm[0] = min(dx, mm[0])
        mm[1] = max(dx, mm[1])
        nn[0] = min(dy, nn[0])
        nn[1] = max(dy, nn[1])
    if dy < 0:
        dy = 0
    elif dy > n:
        dy = n
    if dx < 0:
        dx = 0
    elif dx > m:
        dx = m
    print(nn, mm, dy, dx)
