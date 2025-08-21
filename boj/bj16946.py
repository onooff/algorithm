import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())
board = [[int(x) for x in inputs[i].strip()] for i in range(1, len(inputs))]
memo = [[(-1 if board[i][j] == 1 else 0) for j in range(m)] for i in range(n)]

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
chunk_idx = 1
chunk = dict()


def fill(i, j, chunk_idx):
    global d, memo, n, m, chunk
    q = [(i, j)]
    visited = {(i, j)}
    idx = 0
    while idx < len(q):
        y, x = q[idx]
        for nd in d:
            ny = y + nd[0]
            nx = x + nd[1]
            np = (ny, nx)
            if 0 <= ny < n and 0 <= nx < m and memo[ny][nx] == 0 and np not in visited:
                visited.add(np)
                q.append(np)
        idx += 1
    chunk[chunk_idx] = len(q)
    for p in q:
        y, x = p
        memo[y][x] = chunk_idx


for i in range(n):
    for j in range(m):
        if memo[i][j] == 0:
            fill(i, j, chunk_idx)
            chunk_idx += 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            visited = set()
            for nd in d:
                ny = i + nd[0]
                nx = j + nd[1]
                if (
                    0 <= ny < n
                    and 0 <= nx < m
                    and memo[ny][nx] > 0
                    and memo[ny][nx] not in visited
                ):
                    visited.add(memo[ny][nx])
                    board[i][j] += chunk[memo[ny][nx]]

for line in board:
    print("".join(map(lambda x: str(x % 10), line)))
