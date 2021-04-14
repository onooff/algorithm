def isin(yy, xx, board_size):
    return 0 <= yy < board_size and 0 <= xx < board_size


n, q = map(int, input().split())

size = 2 ** n
board = list()
for i in range(size):
    board.append(list(map(int, input().split())))

ql = list(map(int, input().split()))
for q in ql:
    if q != 0:
        tmp_board = [[0 for j in range(size)] for i in range(size)]
        storm_size = 2 ** q
        for i in range(0, size, storm_size):
            for j in range(0, size, storm_size):
                for a in range(storm_size):
                    for b in range(storm_size):
                        # tmp_board[j+b][i + (storm_size - 1) - a] = board[i + a][j + b]
                        tmp_board[i + b][j + storm_size - 1 - a] = board[i + a][j + b]
        board = tmp_board
    tmp_board = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            around_ice = 0
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny = i + d[0]
                nx = j + d[1]
                if isin(ny, nx, size) and board[ny][nx] > 0:
                    # print(i,j,ny,nx,isin(ny,nx,size))
                    around_ice += 1
            if around_ice < 3:
                # print(i,j,'melt',around_ice)
                tmp_board[i][j] = max(0, board[i][j] - 1)
            else:
                # print(i,j,'not melt',around_ice)
                tmp_board[i][j] = board[i][j]
    board = tmp_board

ans_sum = 0
ans_mass = 0
q = list()
chk = [[False for j in range(size)] for i in range(size)]

for i in range(size):
    for j in range(size):
        ans_sum += board[i][j]
        if board[i][j] > 0 and not chk[i][j]:
            tmp_mass = 0
            q.append((i, j))
            chk[i][j] = True
            while len(q) > 0:
                tmp = q.pop()
                tmp_mass += 1
                y = tmp[0]
                x = tmp[1]
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny = y + d[0]
                    nx = x + d[1]
                    if isin(ny, nx, size) and board[ny][nx] > 0 and not chk[ny][nx]:
                        q.append((ny, nx))
                        chk[ny][nx] = True
            # print(tmp_mass,q,(i,j))
            ans_mass = max(ans_mass, tmp_mass)

# debug
# for i in range(size):
#     print(board[i])

print(ans_sum)
print(ans_mass)
# print(board)
