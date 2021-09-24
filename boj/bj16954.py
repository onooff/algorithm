board = list()
for i in range(8):
    board.append(input())

q = [(7, 0)]
q_idx = 0
ans = 0
chk = [[False for _ in range(8)] for _ in range(8)]

while q_idx < len(q):
    cur = q[q_idx]
    q_idx += 1
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            ny = cur[0]+dy
            nx = cur[1]+dx
            if 0 <= ny < 8 and 0 <= nx < 8 and not chk[ny][nx] and board[ny][nx] == '.' and (ny < 1 or board[ny-1][nx] == '.'):
                if ny == 1:
                    ans = 1
                    break
                chk[ny][nx] = True
                q.append((ny-1, nx))
        if ans == 1:
            break
    if ans == 1:
        break
print(ans)
