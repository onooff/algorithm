import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, degree = map(int, input().split())
    board = list()
    for _ in range(n):
        board.append(list(map(int, input().rstrip().split())))

    y, x = n // 2, n // 2
    for _ in range(abs(degree) // 45):
        for i in range(1, (n // 2) + 1):
            if degree > 0:
                (
                    board[y - i][x],
                    board[y - i][x + i],
                    board[y][x + i],
                    board[y + i][x + i],
                    board[y + i][x],
                    board[y + i][x - i],
                    board[y][x - i],
                    board[y - i][x - i],
                ) = (
                    board[y - i][x - i],
                    board[y - i][x],
                    board[y - i][x + i],
                    board[y][x + i],
                    board[y + i][x + i],
                    board[y + i][x],
                    board[y + i][x - i],
                    board[y][x - i],
                )
            else:
                (
                    board[y - i][x],
                    board[y - i][x + i],
                    board[y][x + i],
                    board[y + i][x + i],
                    board[y + i][x],
                    board[y + i][x - i],
                    board[y][x - i],
                    board[y - i][x - i],
                ) = (
                    board[y - i][x + i],
                    board[y][x + i],
                    board[y + i][x + i],
                    board[y + i][x],
                    board[y + i][x - i],
                    board[y][x - i],
                    board[y - i][x - i],
                    board[y - i][x],
                )
    for b in board:
        print(*b)
