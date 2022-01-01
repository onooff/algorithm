import sys
inputs = sys.stdin.readlines()
colors = list(map(lambda x: tuple(map(int, x.rstrip().split())), inputs[1:-1]))
target_color = tuple(map(int, inputs[-1].rstrip().split()))


def dfs(colors, target_color, idx, n, cur_color, diff):
    if n >= 2:
        tmp = 0
        for i in range(3):
            tmp += abs(cur_color[i]//n-target_color[i])
        diff = min(diff, tmp)
    if n >= 7:
        return diff
    for i in range(idx, len(colors)):
        cur_color[0], cur_color[1], cur_color[2] = cur_color[0] + \
            colors[i][0], cur_color[1]+colors[i][1], cur_color[2]+colors[i][2]
        diff = min(diff, dfs(colors, target_color, i+1, n+1, cur_color, diff))
        cur_color[0], cur_color[1], cur_color[2] = cur_color[0] - \
            colors[i][0], cur_color[1]-colors[i][1], cur_color[2]-colors[i][2]
    return diff


print(dfs(colors, target_color, 0, 0, [0, 0, 0], 999999999))
