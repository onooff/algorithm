n, m = map(int, input().split())
hy, hx = map(int, input().split())
ey, ex = map(int, input().split())
hx -= 1
hy -= 1
ex -= 1
ey -= 1
board = list()
chk = list()
chk_breaked = list()
for i in range(n):
    board.append(list(map(int, input().split())))
    chk.append([9999999 for j in range(m)])
    chk_breaked.append([9999999 for j in range(m)])
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = list()
q.append((hy, hx, False))
chk[hy][hx] = 0

while(len(q) > 0 and (chk[ey][ex] == 9999999 or chk_breaked[ey][ex] == 9999999)):
    tmp = q.pop(0)
    y = tmp[0]
    x = tmp[1]
    is_breaked = tmp[2]

    if(is_breaked):
        step = chk_breaked[y][x]+1
        for i in range(4):
            ny = y+d[i][0]
            nx = x+d[i][1]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0 and chk_breaked[ny][nx] > step:
                q.append((ny, nx, True))
                chk_breaked[ny][nx] = step
                if ny == ey and nx == ex:
                    end = step
                    break
    else:
        step = chk[y][x]+1
        for i in range(4):
            ny = y+d[i][0]
            nx = x+d[i][1]
            if 0 <= ny < n and 0 <= nx < m and chk[ny][nx] > step:
                if board[ny][nx] == 0:
                    q.append((ny, nx, False))
                    chk[ny][nx] = step
                else:
                    q.append((ny, nx, True))
                    chk_breaked[ny][nx] = step
                if ny == ey and nx == ex:
                    end = step
                    break

if chk[ey][ex] == 9999999 and chk_breaked[ey][ex] == 9999999:
    print(-1)
else:
    print(min(chk[ey][ex], chk_breaked[ey][ex]))
