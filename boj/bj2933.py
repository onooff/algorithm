def isin(y, x, r, c):
    return 0 <= y < r and 0 <= x < c


def print_answer(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')
        if i != len(board)-1:
            print()


d = [(1, 0), (0, -1), (0, 1), (-1, 0)]

r, c = map(int, input().split())

board = list()

for i in range(r):
    board.append(list(input()))

n = int(input())
shot_list = list(map(int, input().split()))

for i in range(len(shot_list)):
    h = r - shot_list[i]
    y = -1
    x = -1
    if i % 2 == 0:  # 짝수 = 왼쪽->오른쪽
        for j in range(c):
            if board[h][j] == 'x':
                y = h
                x = j
                break
    else:  # 홀수 = 오른쪽->왼쪽
        for j in range(c-1, -1, -1):
            if board[h][j] == 'x':
                y = h
                x = j
                break
    if y >= 0:
        board[y][x] = '.'
        for j in range(4):
            ny = y+d[j][0]
            nx = x+d[j][1]
            if isin(ny, nx, r, c) and board[ny][nx] == 'x':
                qs = {(ny, nx)}
                ql = [(ny, nx)]
                bfs_idx = 0
                while bfs_idx < len(ql):
                    now_y = ql[bfs_idx][0]
                    now_x = ql[bfs_idx][1]
                    for dd in d:
                        new_y = now_y+dd[0]
                        new_x = now_x+dd[1]
                        if isin(new_y, new_x, r, c) and board[new_y][new_x] == 'x' and (new_y, new_x) not in qs:
                            qs.add((new_y, new_x))
                            ql.append((new_y, new_x))
                    bfs_idx += 1
                # ql.sort(key=lambda x: -x[0])
                # # print(ql)
                # lowest = ql[0][0]
                drop_h = 9999999999999
                for v in ql:
                    if not isin(v[0]+1, v[1], r, c):
                        drop_h = 0
                        break
                    elif board[v[0]+1][v[1]] == '.':
                        drop = 0
                        while isin(v[0]+drop+1, v[1], r, c) and board[v[0]+drop+1][v[1]] == '.':
                            drop += 1
                        if isin(v[0]+drop+1, v[1], r, c) and board[v[0]+drop+1][v[1]] == 'x' and (v[0]+drop+1, v[1]) in qs:
                            continue
                        drop_h = min(drop, drop_h)
                if drop_h > 0:
                    for v in ql:
                        board[v[0]][v[1]] = '.'
                    for v in ql:
                        board[v[0]+drop_h][v[1]] = 'x'
print_answer(board)
