import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
board = inputs[1:]

heart = None
for i in range(n):
    for j in range(n):
        if board[i][j] == "*":
            heart = (i + 1, j)
            break
    if heart != None:
        break

la, ra, b, ll, rl = 0, 0, 0, 0, 0

y = heart[0]
x = heart[1] - 1
while 0 <= x < n and 0 <= y < n and board[y][x] == "*":
    la += 1
    x -= 1

y = heart[0]
x = heart[1] + 1
while 0 <= x < n and 0 <= y < n and board[y][x] == "*":
    ra += 1
    x += 1

y = heart[0] + 1
x = heart[1]
while 0 <= x < n and 0 <= y < n and board[y][x] == "*":
    b += 1
    y += 1

yy = y
xx = x - 1
while 0 <= xx < n and 0 <= yy < n and board[yy][xx] == "*":
    ll += 1
    yy += 1

yy = y
xx = x + 1
while 0 <= xx < n and 0 <= yy < n and board[yy][xx] == "*":
    rl += 1
    yy += 1

print(heart[0] + 1, heart[1] + 1)
print(la, ra, b, ll, rl)
