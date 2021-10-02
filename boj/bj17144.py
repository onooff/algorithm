# n, m, t = map(int, input().split())
# board = list()
# cleaner = list()

# for i in range(n):
#     board.append(list(map(int, input().split())))
#     if board[i][0] == -1:
#         cleaner.append(i)

# d = ((0, 1), (0, -1), (1, 0), (-1, 0))

# for _ in range(t):
#     nboard = [[0 for _ in range(m)] for _ in range(n)]
#     for y in range(n):
#         for x in range(m):
#             o = board[y][x]
#             du = o//5
#             if o <= 0 or du == 0:
#                 nboard[y][x] += o
#                 continue

#             for nd in d:
#                 ny = y+nd[0]
#                 nx = x+nd[1]
#                 if 0 <= ny < n and 0 <= nx < m and nboard[ny][nx] >= 0:
#                     o -= du
#                     nboard[ny][nx] += du
#             nboard[y][x] += o

#     up = True
#     for c in cleaner:
#         y = c
#         x = 0
#         tmp = 0
#         while x+1 < m:
#             x += 1
#             nboard[y][x], tmp = tmp, nboard[y][x]

#         while True:
#             if up:
#                 if y-1 < 0:
#                     break
#                 y -= 1
#             else:
#                 if y+1 >= n:
#                     break
#                 y += 1
#             nboard[y][x], tmp = tmp, nboard[y][x]

#         while x-1 >= 0:
#             x -= 1
#             nboard[y][x], tmp = tmp, nboard[y][x]

#         while True:
#             if up:
#                 y += 1
#             else:
#                 y -= 1
#             if nboard[y][x] == -1:
#                 break
#             nboard[y][x], tmp = tmp, nboard[y][x]
#         up = False
#     board = nboard

# ans = 0
# for i in range(n):
#     ans += sum(board[i])
# print(ans+2)

n, m, t = map(int, input().split())
board = list()
dusts = set()
cleaner = list()

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] > 0:
            dusts.add(i*m+j)
        elif board[i][j] < 0:
            cleaner.append(i*m+j)

d = ((0, 1), (0, -1), (1, 0), (-1, 0))

for _ in range(t):
    nboard = [[0 for _ in range(m)] for _ in range(n)]
    for c in cleaner:
        nboard[c//m][c % m] = -1
    ndusts = set()
    for dust in dusts:
        y = dust//m
        x = dust % m
        o = board[y][x]
        if o == 0:
            continue
        du = o//5
        ndusts.add(dust)
        if du == 0:
            nboard[y][x] += o
            continue

        for nd in d:
            ny = y+nd[0]
            nx = x+nd[1]
            if 0 <= ny < n and 0 <= nx < m and nboard[ny][nx] != -1:
                o -= du
                nboard[ny][nx] += du
                ndusts.add(ny*m+nx)
        nboard[y][x] += o

    up = True
    for c in cleaner:
        y = c//m
        x = (c % m)+1

        tmp = 0
        while x+1 < m:
            nboard[y][x], tmp = tmp, nboard[y][x]
            if nboard[y][x] > 0:
                ndusts.add(y*m+x)
            x += 1

        if up:
            while y-1 >= 0:
                nboard[y][x], tmp = tmp, nboard[y][x]
                if nboard[y][x] > 0:
                    ndusts.add(y*m+x)
                y -= 1
        else:
            while y+1 < n:
                nboard[y][x], tmp = tmp, nboard[y][x]
                if nboard[y][x] > 0:
                    ndusts.add(y*m+x)
                y += 1

        while x-1 >= 0:
            nboard[y][x], tmp = tmp, nboard[y][x]
            if nboard[y][x] > 0:
                ndusts.add(y*m+x)
            x -= 1

        if up:
            while nboard[y][x] != -1:
                nboard[y][x], tmp = tmp, nboard[y][x]
                if nboard[y][x] > 0:
                    ndusts.add(y*m+x)
                y += 1
        else:
            while nboard[y][x] != -1:
                nboard[y][x], tmp = tmp, nboard[y][x]
                if nboard[y][x] > 0:
                    ndusts.add(y*m+x)
                y -= 1
        if up:
            up = False
    board = nboard
    dusts = ndusts

ans = 0
for i in range(n):
    ans += sum(board[i])
print(ans+2)
