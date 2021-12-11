y, x, k = map(int, input().split())
board = [[0 for _ in range(x)] for _ in range(y)]
for _ in range(k):
    xmin, ymin, xmax, ymax = map(int, input().split())
    for i in range(ymin, ymax):
        for j in range(xmin, xmax):
            board[i][j] = 1
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = list()
for i in range(y):
    for j in range(x):
        if board[i][j] == 0:
            cur = i*x+j
            board[i][j] = 1
            q = [cur]
            idx = 0
            while idx < len(q):
                cur = q[idx]
                idx += 1
                cury, curx = cur//x, cur % x
                for nd in d:
                    ny = cury+nd[0]
                    nx = curx+nd[1]
                    if 0 <= ny < y and 0 <= nx < x and board[ny][nx] == 0:
                        board[ny][nx] = 1
                        q.append(ny*x+nx)
            ans.append(len(q))
ans.sort()
print(len(ans))
for area in ans:
    print(area, end=' ')
