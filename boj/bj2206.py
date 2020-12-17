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
