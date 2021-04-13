'''
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0
'''


def isin(y, x, n):
    return y >= 0 and x >= 0 and y < n and x < n


n = int(input())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))


y = n//2
x = n//2
go = 0
ans = 0

d = [(-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1),
     (1, -1, 0.1), (-1, 1, 0.01), (1, 1, 0.01), (0, -2, 0.05), (0, -1, -1)]
tonado_d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
move_dust_d = [(0, 1, 1, 1), (1, 0, -1, 1), (0, 1, 1, -1), (1, 0, 1, 1)]
# 좌 ny=y+[i][0] nx=x+d[i][1]
# 하 ny=y-[i][1] nx=x+d[i][0]
# 우 ny=y+[i][0] nx=x-d[i][1]
# 상 ny=y+[i][1] nx=x+d[i][0]

go = 0
answer = 0
for i in range(n*2-1):
    td = i % 4

    if td % 2 == 0:
        go += 1

    for j in range(go):
        y += tonado_d[td][0]
        x += tonado_d[td][1]
        if board[y][x] == 0:
            # print('pass')
            continue
        s = 0
        # print('>>>', y, x, board[y][x], ':', end='')
        for k in range(len(d)):
            target_y = y+(d[k][move_dust_d[td][0]]*move_dust_d[td][2])
            target_x = x+(d[k][move_dust_d[td][1]]*move_dust_d[td][3])
            move_dust = int(board[y][x]*d[k][2])
            # print(move_dust, end=' ')
            if move_dust >= 0:
                if isin(target_y, target_x, n):
                    board[target_y][target_x] += move_dust
                else:
                    answer += move_dust
                s += move_dust
            else:
                move_dust = board[y][x]-s
                if isin(target_y, target_x, n):
                    board[target_y][target_x] += move_dust
                else:
                    answer += move_dust
        board[y][x] = 0
        # print()
        # for i in range(n):
        #     print(board[i])

print(answer)
# for i in range(n):
#     print(board[i])
