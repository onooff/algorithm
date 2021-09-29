import sys
inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].rstrip().split())
r, c, d = map(int, inputs[1].rstrip().split())
chk = [[False for _ in range(m)] for _ in range(n)]
wall = set()
for i in range(2, n+2):
    j = 0
    for state in list(map(int, inputs[i].rstrip().split())):
        if state == 1:
            chk[i-2][j] = True
            wall.add((i-2, j))
        j += 1

dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
dnd = {0: 3, 3: 2, 2: 1, 1: 0}

ans = 0
while True:
    if not chk[r][c]:
        chk[r][c] = True
        ans += 1
    go = False
    nd = d
    for cnt in range(1, 5):
        nd = dnd[nd]
        nr = r+dd[nd][0]
        nc = c+dd[nd][1]
        if 0 <= nr < n and 0 <= nc < m and not chk[nr][nc]:
            d = nd
            go = True
            break
    if go:
        r = nr
        c = nc
    else:
        nr = r-dd[d][0]
        nc = c-dd[d][1]
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in wall:
            r = nr
            c = nc
        else:
            break
print(ans)
