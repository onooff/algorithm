def go(board, y, x, h):
    if h == 3:
        board[y][x] = '*'
        board[y+1][x-1] = '*'
        board[y+1][x+1] = '*'
        for j in range(x-2, x+3):
            board[y+2][j] = '*'
        return
    h2 = h//2
    go(board, y, x, h2)
    go(board, y+h2, x-h2, h2)
    go(board, y+h2, x+h2, h2)
    return


n = int(input())
w = 6*(n//3)
board = [[' ' for j in range(w)] for i in range(n)]
go(board, 0, w//2, n)
for i in range(n):
    print(''.join(board[i][1:]))
