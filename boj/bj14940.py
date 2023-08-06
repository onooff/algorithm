import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())

board = [list(map(int, inputs[i].rstrip().split())) for i in range(1, len(inputs))]
ans = [["-1" for _ in range(m)] for _ in range(n)]

q = None
nq = []
dis = "0"
visited = None
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q = [(i, j)]
            visited = set(q)
        elif board[i][j] == 0:
            ans[i][j] = "0"

while len(q) > 0:
    cur = q.pop()
    y = cur[0]
    x = cur[1]
    ans[y][x] = dis
    for nd in d:
        ny = y + nd[0]
        nx = x + nd[1]
        nxt = (ny, nx)
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 0 and nxt not in visited:
            visited.add(nxt)
            nq.append(nxt)

    if len(q) == 0:
        q = nq
        nq = []
        dis = str(int(dis) + 1)

for a in ans:
    print(" ".join(a))
