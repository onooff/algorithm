def solution(m, n, puddles):
    board = [[1 for _ in range(m)]for _ in range(n)]
    for p in puddles:
        board[p[1]-1][p[0]-1] = 0
    for i in range(1, n):
        if board[i][0] != 0:
            board[i][0] = board[i-1][0]
    for j in range(1, m):
        if board[0][j] != 0:
            board[0][j] = board[0][j-1]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] != 0:
                board[i][j] = board[i-1][j]+board[i][j-1]
    for b in board:
        print(b)
    return board[n-1][m-1]


print(solution(5, 5, [[2, 1], [1, 2]]))
