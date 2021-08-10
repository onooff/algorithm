def isin(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def solution(maps):
    inf = 999999999
    n = len(maps)
    m = len(maps[0])
    chk = [[inf for j in range(m)] for i in range(n)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(0, 0)]
    chk[0][0] = 1
    while len(q) > 0:
        now = q.pop(0)
        a = chk[now[0]][now[1]]+1
        for dd in d:
            ny = now[0]+dd[0]
            nx = now[1]+dd[1]
            if isin(ny, nx, n, m) and maps[ny][nx] > 0 and chk[ny][nx] > a:
                if ny == n-1 and nx == m-1:
                    return a
                q.append((ny, nx))
                chk[ny][nx] = a
    return -1
