import sys

inputs = sys.stdin.readlines()
r, c, n = map(int, inputs[0].rstrip().split())

default_board = list(map(lambda x: list(x.rstrip()), inputs[1:]))
full_board = [["O" for _ in range(c)] for _ in range(r)]

d = ((0, 1), (0, -1), (1, 0), (-1, 0))


def boom(bomb_set_board, d):
    r = len(bomb_set_board)
    c = len(bomb_set_board[0])
    ret_borad = [["O" for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if bomb_set_board[i][j] == "O":
                ret_borad[i][j] = "."
                for nd in d:
                    ni = i + nd[0]
                    nj = j + nd[1]
                    if 0 <= ni < r and 0 <= nj < c:
                        ret_borad[ni][nj] = "."
    return ret_borad


boom_board_1 = boom(default_board, d)
boom_board_2 = boom(boom_board_1, d)


ans = None
if n == 1:
    ans = default_board
elif n % 2 == 0:
    ans = full_board
elif n % 4 == 3:
    ans = boom_board_1
else:
    ans = boom_board_2

for a in ans:
    sys.stdout.write("".join(a) + "\n")
