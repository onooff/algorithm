import heapq
import math

n = int(input())
chk = [[math.inf for i in range(n)] for i in range(n)]
chk[0][0] = 0
board = list()
for i in range(n):
    board.append(input())

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
q = [(0, 0, 0)]
while len(q) > 0:
    cur = heapq.heappop(q)
    for nd in d:
        ny = cur[1]+nd[0]
        nx = cur[2]+nd[1]
        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] == '0' and chk[ny][nx] > cur[0]+1:
                chk[ny][nx] = cur[0]+1
                heapq.heappush(q, (chk[ny][nx], ny, nx))
            elif board[ny][nx] == '1' and chk[ny][nx] > cur[0]:
                chk[ny][nx] = cur[0]
                heapq.heappush(q, (chk[ny][nx], ny, nx))

print(chk[n-1][n-1])
