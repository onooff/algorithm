n = int(input())
w = 0
h = 0
for i in range(n-1):
    w += 2**(i+1)
    h += 2**i
w = w*2+1
h = h*2+1
board = [[' ' for _ in range(w)] for _ in range(h)]

x = w//2
if n % 2 == 0:
    y = h-1
    d = -1
else:
    y = 0
    d = 1

tmp_h = h
for go in range(n-1, -1, -1):
    board[y][x] = '*'
    for i in range(1, tmp_h):
        y += d
        if i == tmp_h-1:
            for j in range(x-i, x+i+1):
                board[y][j] = '*'
        else:
            board[y][x-i] = '*'
            board[y][x+i] = '*'

    d *= -1
    y += d
    tmp_h -= 2**go

for i in range(h):
    print(''.join(board[i]).rstrip())
