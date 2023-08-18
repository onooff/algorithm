import sys
import heapq

input = sys.stdin.readline

inf = float("inf")
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

tc = 0
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break

    board = [list(map(int, input().rstrip().split())) for i in range(n)]
    q = [(board[0][0], 0, 0)]
    while True:
        value, y, x = heapq.heappop(q)
        if y == n - 1 and x == n - 1:
            break

        for nd in d:
            ny = y + nd[0]
            nx = x + nd[1]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > -1:
                heapq.heappush(q, (value + board[ny][nx], ny, nx))
                board[ny][nx] = -1
    print(f"Problem {tc}: {value}")
