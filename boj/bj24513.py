q = list()
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = [0, 0, 0, 0]

n, m = map(int, input().split())
board = list()
chk = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] != 0:
            chk[i][j] = True
            if board[i][j] > 0:
                q.append(i*m+j)
                ans[board[i][j]] += 1

while len(q) > 0:
    new_q = list()
    new_chk = {1: set(), 2: set()}
    for cur in q:
        y = cur//m
        x = cur % m
        v = board[y][x]
        if v >= 3:
            continue
        for nd in d:
            ny = y+nd[0]
            nx = x+nd[1]
            if 0 <= ny < n and 0 <= nx < m and not chk[ny][nx]:
                cood = ny*m+nx
                if cood not in new_chk[v]:
                    new_chk[v].add(cood)
                    new_q.append(cood)
                    board[ny][nx] += v

    for k in new_chk:
        for cood in new_chk[k]:
            y = cood//m
            x = cood % m
            if not chk[y][x]:
                chk[y][x] = True
                ans[board[y][x]] += 1
    q = new_q

print(ans[1], ans[2], ans[3])
