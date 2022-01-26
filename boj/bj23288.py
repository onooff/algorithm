dice = [6, 3, 1, 4]
dice_side = [5, 2]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 동남서북

n, m, k = map(int, input().split())

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))
d_board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if d_board[i][j] != 0:
            continue
        d_board[i][j] = -1
        q = [(i, j)]
        idx = 0
        while idx < len(q):
            cur = q[idx]
            for nd in d:
                ny = cur[0]+nd[0]
                nx = cur[1]+nd[1]
                if 0 <= ny < n and 0 <= nx < m and d_board[ny][nx] == 0 and board[ny][nx] == board[i][j]:
                    d_board[ny][nx] = -1
                    q.append((ny, nx))
            idx += 1
        for v in q:
            d_board[v[0]][v[1]] = len(q)
cur_y, cur_x, cur_d = 0, 0, 0
point = 0
for _ in range(k):
    nxt_y = cur_y+d[cur_d][0]
    nxt_x = cur_x+d[cur_d][1]
    if not(0 <= nxt_y < n and 0 <= nxt_x < m):
        cur_d = (cur_d+2) % 4
        dice[1], dice[3], dice_side[0], dice_side[1] = dice[3], dice[1], dice_side[1], dice_side[0]
        nxt_y = cur_y + d[cur_d][0]
        nxt_x = cur_x + d[cur_d][1]
    dice.append(dice.pop(0))
    cur_y, cur_x = nxt_y, nxt_x
    point += board[cur_y][cur_x]*d_board[cur_y][cur_x]
    if dice[0] > board[cur_y][cur_x]:
        cur_d = (cur_d+1) % 4
        dice[1], dice[3], dice_side[0], dice_side[1] = dice_side[0], dice_side[1], dice[3], dice[1]
    elif dice[0] < board[cur_y][cur_x]:
        cur_d = 3 if cur_d == 0 else cur_d-1
        dice[1], dice[3], dice_side[0], dice_side[1] = dice_side[1], dice_side[0], dice[1], dice[3]

print(point)
