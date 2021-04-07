def solution(board):
    answer = 0
    by = len(board)
    bx = len(board[0])
    chk = list()
    for i in range(by):
        chk.append(list())
        for j in range(bx):
            if board[i][j] != 0:
                chk[i].append(-1)
            else:
                chk[i].append(99999999999)
    chk[0][0] = 0
    # print(by, bx, len(chk))

    q = list()
    q.append((0, 0, -1, 0))

    while len(q) > 0:
        tmp = q.pop(0)
        y = tmp[0]
        x = tmp[1]
        last_d = tmp[2]
        money = tmp[3]
        for d in [[0, 1, 0], [0, -1, 1], [1, 0, 2], [-1, 0, 3]]:
            ny = y+d[0]
            nx = x+d[1]
            nd = d[2]
            if ny >= 0 and nx >= 0 and ny < by and nx < bx and board[ny][nx] == 0:
                if nd != last_d and last_d != -1:
                    nmoney = money+600
                else:
                    nmoney = money+100
                if chk[ny][nx] >= nmoney:
                    q.append((ny, nx, nd, nmoney))
                    chk[ny][nx] = nmoney

    # for i in range(by):
    #     for j in range(bx):
    #         print(chk[i][j], end='  ')
    #     print('')
    return chk[by-1][bx-1]


print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
