t = int(input())

for tc in range(t):
    input()
    n, m = map(int, input().split())
    board = [[0 for i in range(n)] for i in range(2)]
    board[0].append(1)
    board[1].append(1)
    for i in range(m):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        board[y][x] = 1
    # print(board)
    is_ok = True
    for i in range(n):
        if not((board[0][i] == 0 and board[1][i] == 0) or (board[0][i] == 0 and board[1][i] == 0)):
            if board[0][i] == 0:
                if board[0][i+1] == 1:
                    is_ok = False
                    break
                else:
                    board[0][i+1] = 1
            elif board[1][i] == 0:
                if board[1][i+1] == 1:
                    is_ok = False
                    break
                else:
                    board[1][i+1] = 1

    if is_ok:
        print('YES')
    else:
        print('NO')
