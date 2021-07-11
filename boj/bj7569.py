d = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
n, m, h = map(int, input().split())

board = list()
cnt = n*m*h
q = list()
t = 0

qlen = 0
for i in range(h):
    board.append(list())
    for j in range(m):
        board[i].append(list(map(int, input().split())))
        for k in range(n):
            if board[i][j][k] == -1:
                cnt -= 1
            elif board[i][j][k] == 1:
                q.append((i, j, k, t))
                cnt -= 1
                qlen += 1

now = 0
while qlen > now:
    tmp = q[now]
    z = tmp[0]
    y = tmp[1]
    x = tmp[2]
    t = tmp[3]
    for dd in d:
        nz = z+dd[0]
        ny = y+dd[1]
        nx = x+dd[2]
        if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = 1
            cnt -= 1
            q.append((nz, ny, nx, t+1))
            qlen += 1
    now += 1

if cnt > 0:
    print(-1)
else:
    print(t)
