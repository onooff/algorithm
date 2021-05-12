def is_in(i, j, n):
    return 0 <= i < n and 0 <= j < n


n, m = map(int, input().split())
board = list()
chk = list()
for i in range(n):
    board.append(list(map(int, input().split())))
    chk.append([False for j in range(n)])

stk = list()
i = 0
j = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
nd = 0
while not(i == n//2 and j == n//2):
    chk[i][j] = True
    if board[i][j] != 0:
        stk.append(board[i][j])
    ni = i+d[nd][0]
    nj = j+d[nd][1]
    if not(is_in(ni, nj, n) and not chk[ni][nj]):
        nd = (nd+1) % 4
        ni = i+d[nd][0]
        nj = j+d[nd][1]
    i = ni
    j = nj
stk.reverse()
# print(stk, len(stk))
ans = 0
nd = [3, 1, 0, 2]
for go in range(m):
    d, s = map(int, input().split())
    d -= 1
    d = nd[d]
    cnt = -1
    now = -1
    next_d = 1
    while s > 0:
        cnt += 1
        now += next_d
        if now >= len(stk):
            break
        if cnt % 4 == 0 or cnt % 4 == 3:
            next_d += 1
        # print(now)
        if d == cnt % 4:
            stk[now] = 0
            s -= 1
    flag = True
    while flag:
        flag = False
        new_stk = list()
        pop_cnt = 1
        # print(stk)
        for ball in stk:
            # print(ball)
            if ball == 0:
                continue
            if len(new_stk) > 0:
                if new_stk[-1] == ball:
                    pop_cnt += 1
                else:
                    if pop_cnt >= 4:
                        flag = True
                        ans += pop_cnt*new_stk[-1]
                        # print('>>>pop!', new_stk[-1], pop_cnt, ans, stk)
                        for poppop in range(pop_cnt):
                            new_stk.pop()
                    pop_cnt = 1
            new_stk.append(ball)
        if pop_cnt >= 4:
            flag = True
            ans += pop_cnt*new_stk[-1]
            # print('>>>pop!', new_stk[-1], pop_cnt, ans)
            for poppop in range(pop_cnt):
                new_stk.pop()
        stk = new_stk
        if len(stk) > (n*n-1):
            stk = stk[:n*n-1]
    if len(stk) == 0:
        break
    new_stk = list()
    ball_num = stk[0]
    ball_cnt = 0
    for ball in stk:
        if ball_num == ball:
            ball_cnt += 1
        else:
            new_stk.append(ball_cnt)
            new_stk.append(ball_num)
            ball_num = ball
            ball_cnt = 1
    new_stk.append(ball_cnt)
    new_stk.append(ball_num)
    stk = new_stk
    if len(stk) > (n*n-1):
        stk = stk[:n*n-1]
    # print('>>>', stk)
print(ans)
