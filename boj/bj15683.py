import sys

inputs = sys.stdin.readlines()

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
cam_ranges = (
    None,
    ((0,), (1,), (2,), (3,)),
    ((0, 2), (1, 3)),
    ((0, 1), (1, 2), (2, 3), (3, 0)),
    ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
    ((0, 1, 2, 3),),
)
board = [list(map(int, line.split())) for line in inputs[1:]]

minn = 0
cameras = list()
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 0:
            minn += 1
        elif board[i][j] < 6:
            cameras.append((board[i][j], i, j))

# 5번, 2번, 나머지 카메라 순서로 dfs하기 위해 정렬
cameras.sort(key=lambda x: ((0 if x[0] == 5 else 1 if x[0] == 2 else 2), x[0]))
# print(cameras)


def check(d, board, cam_range, val, y, x):
    ret = 0
    for dir in cam_range:
        ny = y + d[dir][0]
        nx = x + d[dir][1]
        while (
            (0 <= ny < len(board)) and (0 <= nx < len(board[0])) and board[ny][nx] != 6
        ):
            if not (1 <= board[ny][nx] <= 5):
                board[ny][nx] += val
                if (val == -1 and board[ny][nx] == -1) or (
                    val == 1 and board[ny][nx] == 0
                ):
                    ret += 1
            ny += d[dir][0]
            nx += d[dir][1]
    return ret


def dfs(d, cam_ranges, board, cameras, cur, minn):
    ret = minn
    if cur >= len(cameras):
        return ret

    cam_num = cameras[cur][0]
    y = cameras[cur][1]
    x = cameras[cur][2]
    cam_range = cam_ranges[cam_num]
    for cr in cam_range:
        minn -= check(d, board, cr, -1, y, x)
        ret = min(ret, dfs(d, cam_ranges, board, cameras, cur + 1, minn))
        minn += check(d, board, cr, 1, y, x)

    return ret


print(dfs(d, cam_ranges, board, cameras, 0, minn))
