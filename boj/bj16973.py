def isin(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def isinhw(y, x, h, w, n, m):
    return 0 <= y < n and 0 <= x < m and 0 <= y+h-1 < n and 0 <= x+w-1 < m


n, m = map(int, input().split())
board = list()
chk = list()
for i in range(n):
    chk.append([False for j in range(m)])
    board.append(list(map(int, input().split())))

h, w, sy, sx, fy, fx = map(int, input().split())
sy -= 1
sx -= 1
fy -= 1
fx -= 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            for a in range(i-(h-1), i+1):
                for b in range(j-(w-1), j+1):
                    if isin(a, b, n, m):
                        chk[a][b] = True

q = list()
q.append((sy, sx, 0))
chk[sy][sx] = True
ans = -1
while len(q) > 0:
    tmp = q.pop(0)
    # print(tmp)
    if tmp[0] == fy and tmp[1] == fx:
        ans = tmp[2]
        break
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny = tmp[0]+d[0]
        nx = tmp[1]+d[1]
        if isinhw(ny, nx, h, w, n, m) and not chk[ny][nx]:
            chk[ny][nx] = True
            q.append((ny, nx, tmp[2]+1))
print(ans)
