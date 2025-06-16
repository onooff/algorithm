import sys

board = list(map(lambda x: x.strip(), sys.stdin.readlines()[1:]))
N, M = len(board), len(board[0])
start = None
for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            start = (i, j)
            break
    if start != None:
        break

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[start[0]][start[1]] = True
q = [start]
ans = 0
while len(q) > 0:
    cur = q.pop(0)
    for dd in d:
        ny = cur[0] + dd[0]
        nx = cur[1] + dd[1]
        if (
            (0 <= ny < N)
            and (0 <= nx < M)
            and (not visited[ny][nx])
            and (board[ny][nx] != "X")
        ):
            if board[ny][nx] == "P":
                ans += 1
            visited[ny][nx] = True
            q.append((ny, nx))
if ans == 0:
    print("TT")
else:
    print(ans)
