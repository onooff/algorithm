def isin(y, x, h, w):
    return 0 <= y < h and 0 <= x < w


t = int(input())

for tc in range(t):
    h, w = map(int, input().split())
    board = list()
    chk = [[False for j in range(w)] for i in range(h)]
    for i in range(h):
        board.append(list(input()))
        for j in range(w):
            if board[i][j] == '*':
                chk[i][j] = True

    k = input()
    key_set = set()
    if k != '0':
        key_set = set(list(k))

    # for i in range(h):
    #     print(board[i])
    # print(key_set)

    ans = 0
    q = list()
    locked_set = set()

    ############ 입구찾기 ##############
    for i in [0, h - 1]:
        for j in range(w):
            if not chk[i][j]:
                c = board[i][j]
                if str.isalpha(c):
                    if str.islower(c):
                        key_set.add(c)
                        q.append((i, j))
                        chk[i][j] = True
                    else:
                        locked_set.add((i, j))
                else:
                    q.append((i, j))
                    chk[i][j] = True
    for j in [0, w - 1]:
        for i in range(h):
            if not chk[i][j]:
                c = board[i][j]
                if str.isalpha(c):
                    if str.islower(c):
                        key_set.add(c)
                        q.append((i, j))
                        chk[i][j] = True
                    else:
                        locked_set.add((i, j))
                else:
                    q.append((i, j))
                    chk[i][j] = True

    ############ 탐색시작 ##############
    # print(q)
    # print(locked_q)
    # print(key_set)
    while True:
        tmp_set = set()
        for door in locked_set:
            if str.lower(board[door[0]][door[1]]) in key_set:
                q.append(door)
            else:
                tmp_set.add(door)
        locked_set = tmp_set

        if len(q) == 0:
            break

        while len(q) > 0:
            # for i in range(h):
            #     print(chk[i])
            # print()
            tmp = q.pop(0)
            y = tmp[0]
            x = tmp[1]
            if board[y][x] == '$':
                ans += 1
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = y + d[0]
                nx = x + d[1]
                if isin(ny, nx, h, w) and not chk[ny][nx]:
                    c = board[ny][nx]
                    if str.isalpha(c):
                        if str.islower(c):
                            key_set.add(c)
                            q.append((ny, nx))
                            chk[ny][nx] = True
                        else:
                            if str.lower(c) in key_set:
                                q.append((ny, nx))
                                chk[ny][nx] = True
                            else:
                                locked_set.add((ny, nx))
                    else:
                        q.append((ny, nx))
                        chk[ny][nx] = True
    print(ans)
