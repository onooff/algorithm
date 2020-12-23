n = int(input())
ans_m1 = 0
ans_0 = 0
ans_1 = 0
ds = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2]
]
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))


def dfs(y, x, l):
    # print(">>>dfs", y, x, l, end='')
    global ans_m1, ans_0, ans_1, ds, board
    c = board[y][x]
    if l == 1:
        # print(' good', c)
        if c == 0:
            ans_0 += 1
        elif c == -1:
            ans_m1 += 1
        else:
            ans_1 += 1
        return

    is_good = True
    for i in range(l):
        for j in range(l):
            if board[y+i][x+j] != c:
                is_good = False
                break
        if not is_good:
            break
    if is_good:
        # print(' good', c)
        if c == 0:
            ans_0 += 1
        elif c == -1:
            ans_m1 += 1
        else:
            ans_1 += 1
    else:
        # print(' cut')
        nl = l//3
        for d in ds:
            ny = y+(d[0]*nl)
            nx = x+(d[1]*nl)
            dfs(ny, nx, nl)


dfs(0, 0, n)
print(ans_m1)
print(ans_0)
print(ans_1)
