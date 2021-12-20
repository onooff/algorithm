import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].rstrip().split())
board = list()
aircon = list()
for i in range(1, len(inputs)):
    board.append(list(map(int, inputs[i].rstrip().split())))
    i -= 1
    for j in range(m):
        if board[i][j] == 9:
            aircon.append(i * m + j)

d = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 상우하좌
d_v = {0: -m, 1: 1, 2: m, 3: -1}  # 상우하좌
chk = set(aircon)
d_chk = {0: set(aircon), 1: set(aircon), 2: set(aircon), 3: set(aircon)}
next_d = {
    0: {0: 0, 1: 1, 2: 2, 3: 3},
    1: {0: 0, 1: 3, 2: 2, 3: 1},
    2: {0: 2, 1: 1, 2: 0, 3: 3},
    3: {0: 1, 1: 0, 2: 3, 3: 2},
    4: {0: 3, 1: 2, 2: 1, 3: 0},
    # 9: {0: 0, 1: 1, 2: 2, 3: 3},
}
for a in aircon:
    y, x = a // m, a % m
    for cur_d in d:
        cur_y = y + d[cur_d][0]
        cur_x = x + d[cur_d][1]
        cur_v = cur_y * m + cur_x
        while 0 <= cur_y < n and 0 <= cur_x < m and cur_v not in d_chk[cur_d]:
            chk.add(cur_v)
            d_chk[cur_d].add(cur_v)
            if (
                board[cur_y][cur_x] == 9
                or (board[cur_y][cur_x] == 1 and cur_d % 2 == 1)
                or (board[cur_y][cur_x] == 2 and cur_d % 2 == 0)
            ):
                break
            cur_d = next_d[board[cur_y][cur_x]][cur_d]
            cur_y += d[cur_d][0]
            cur_x += d[cur_d][1]
            cur_v += d_v[cur_d]
print(len(chk))


# aa = [["□" for _ in range(m)] for _ in range(n)]
# for c in chk:
#     aa[c // m][c % m] = "■"

# for a in aa:
#     print("".join(a))
