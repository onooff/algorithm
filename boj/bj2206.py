import sys
import math

inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].split())
board = list(map(lambda x: x.rstrip(), inputs[1:]))

chk = [[math.inf for _ in range(m)] for _ in range(n)]

q = [0]
chk[0][0] = 1
idx = 0
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
walls = list()
while idx < len(q):
    cur = q[idx]
    y = cur//m
    x = cur % m
    next_step = chk[y][x]+1
    for nd in d:
        ny = y+nd[0]
        nx = x+nd[1]
        if 0 <= ny < n and 0 <= nx < m and chk[ny][nx] > next_step:
            chk[ny][nx] = next_step
            nxt = ny*m+nx
            if board[ny][nx] == '1':
                walls.append(nxt)
            else:
                q.append(nxt)
    idx += 1

q = walls
idx = 0
while idx < len(q):
    cur = q[idx]
    y = cur//m
    x = cur % m
    next_step = chk[y][x]+1
    for nd in d:
        ny = y+nd[0]
        nx = x+nd[1]
        if 0 <= ny < n and 0 <= nx < m and chk[ny][nx] > next_step and board[ny][nx] == '0':
            chk[ny][nx] = next_step
            q.append(ny*m+nx)
    idx += 1

if chk[n-1][m-1] == math.inf:
    chk[n-1][m-1] = -1
print(chk[n-1][m-1])

'''
def isIn(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


d = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]

n, m = map(int, input().split())
board = list()
chk_not_break = list()
chk_break = list()

for i in range(n):
    tmp = input()
    board.append(list())
    chk_not_break.append(list())
    chk_break.append(list())
    for j in range(m):
        board[i].append(int(tmp[j]))
        chk_not_break[i].append(0)
        chk_break[i].append(0)

# for i in range(n):
#     print(board[i])
# for i in range(n):
#     print(chk[i])


bfs = list()
chk_not_break[0][0] = 1
ans = -1
bfs.append((0, 0, False, 1))
while len(bfs) > 0:
    # print(bfs)
    tmp = bfs.pop(0)
    if tmp[0] == n-1 and tmp[1] == m-1:
        ans = tmp[3]
        break
    nd = tmp[3]+1
    is_breaked = tmp[2]
    if is_breaked:
        for k in range(4):
            ni = tmp[0]+d[k][0]
            nj = tmp[1]+d[k][1]
            if isIn(ni, nj, n, m):
                if not chk_break[ni][nj]:
                    if board[ni][nj] == 0:
                        # print(ni, nj)
                        chk_break[ni][nj] = True
                        bfs.append((ni, nj, tmp[2], tmp[3]+1))
    else:
        for k in range(4):
            ni = tmp[0]+d[k][0]
            nj = tmp[1]+d[k][1]
            if isIn(ni, nj, n, m):
                if not chk_not_break[ni][nj]:
                    if board[ni][nj] == 0:
                        # print(ni, nj)
                        chk_not_break[ni][nj] = True
                        bfs.append((ni, nj, tmp[2], tmp[3]+1))
                    elif not tmp[2]:
                        chk_break[ni][nj] = True
                        bfs.append((ni, nj, True, tmp[3]+1))


print(ans)
'''
