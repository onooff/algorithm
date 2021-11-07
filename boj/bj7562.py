d = ((2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
t = int(input())
for _ in range(t):
    n = int(input())
    y, x = map(int, input().split())
    ey, ex = map(int, input().split())
    chk = [[-1 for _ in range(n)] for _ in range(n)]

    q = [y*n+x]
    idx = 0
    chk[y][x] = 0
    ans = 0

    while idx < len(q) and chk[ey][ex] < 0:
        y = q[idx]//n
        x = q[idx] % n
        idx += 1
        for nd in d:
            ny = y+nd[0]
            nx = x+nd[1]
            if 0 <= ny < n and 0 <= nx < n and chk[ny][nx] < 0:
                q.append(ny*n+nx)
                chk[ny][nx] = chk[y][x]+1

    print(chk[ey][ex])
