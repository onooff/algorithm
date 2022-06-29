squares = set()
num = 0
sq = num*num
while sq < 1000000000:
    squares.add(sq)
    num += 1
    sq = num*num

n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(input())

ans = -1
for i in range(n):
    for j in range(m):
        tmp = int(board[i][j])
        if tmp in squares:
            ans = max(ans, tmp)
        for di in range(-8, 9):
            for dj in range(0, 9):
                s = board[i][j]
                if not (di == 0 and dj == 0):
                    ni = i+di
                    nj = j+dj
                    while 0 <= ni < n and 0 <= nj < m:
                        s += board[ni][nj]
                        # print(s)
                        tmp = int(s)
                        if tmp in squares:
                            ans = max(ans, tmp)
                        tmp = int(s[::-1])
                        if tmp in squares:
                            ans = max(ans, tmp)
                        ni += di
                        nj += dj
print(ans)
