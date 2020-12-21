def isIn(i, j, y, x):
    if i >= 0 and j >= 0 and i < y and j < x:
        return True
    return False


d = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]

n = int(input())

board = list()
chk_RGB = list()
chk_RB = list()
for i in range(n):
    board.append(list(input()))
    chk_RGB.append(list())
    chk_RB.append(list())
    for j in range(n):
        chk_RGB[i].append(False)
        chk_RB[i].append(False)
    # print(board[i])

bfs_RGB = list()
RGBcnt = 0
bfs_RB = list()
RBcnt = 0

# chk_RGB[0][0] = True
# bfs_RGB.append((0,0))
# chk_RB[0][0] = True
# bfs_RB.append((0,0))


for i in range(n):
    for j in range(n):
        if not chk_RGB[i][j]:
            RGBcnt += 1
            chk_RGB[i][j] = True
            bfs_RGB.append((i, j))
            color = board[i][j]
            while len(bfs_RGB) != 0:
                tmp = bfs_RGB.pop(0)
                for nd in d:
                    ni = tmp[0]+nd[0]
                    nj = tmp[1]+nd[1]
                    if isIn(ni, nj, n, n) and board[ni][nj] == color and not chk_RGB[ni][nj]:
                        chk_RGB[ni][nj] = True
                        bfs_RGB.append((ni, nj))
        if not chk_RB[i][j]:
            RBcnt += 1
            chk_RB[i][j] = True
            bfs_RB.append((i, j))
            color = board[i][j]
            if color == 'B':
                while len(bfs_RB) != 0:
                    tmp = bfs_RB.pop(0)
                    for nd in d:
                        ni = tmp[0]+nd[0]
                        nj = tmp[1]+nd[1]
                        if isIn(ni, nj, n, n) and board[ni][nj] == color and not chk_RB[ni][nj]:
                            chk_RB[ni][nj] = True
                            bfs_RB.append((ni, nj))
            else:
                while len(bfs_RB) != 0:
                    tmp = bfs_RB.pop(0)
                    for nd in d:
                        ni = tmp[0]+nd[0]
                        nj = tmp[1]+nd[1]
                        if isIn(ni, nj, n, n) and board[ni][nj] != 'B' and not chk_RB[ni][nj]:
                            chk_RB[ni][nj] = True
                            bfs_RB.append((ni, nj))
print(RGBcnt, RBcnt)
# print(chk_RB, chk_RGB)
