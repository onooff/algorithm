import sys


def turn(h, w, sticker):
    for i in range(len(sticker)):
        sticker[i][0], sticker[i][1] = sticker[i][1], (h - 1) - sticker[i][0]


inputs = sys.stdin.readlines()
n, m, k = map(int, inputs[0].rstrip().split())
board = [[False for _ in range(m)] for _ in range(n)]
idx = 1
ans = 0
for _ in range(k):
    h, w = map(int, inputs[idx].rstrip().split())
    idx += 1
    sticker = list()
    for i in range(h):
        tmp = list(map(int, inputs[idx].rstrip().split()))
        idx += 1
        for j in range(w):
            if tmp[j] == 1:
                sticker.append([i, j])

    for tryy in range(4):
        is_ok = False
        ok_i = -1
        ok_j = -1
        for i in range(n - h + 1):
            for j in range(m - w + 1):
                is_ok = True
                for s in sticker:
                    if board[i + s[0]][j + s[1]]:
                        is_ok = False
                        break
                if is_ok:
                    ok_i = i
                    ok_j = j
                    break
            if is_ok:
                break
        if is_ok:
            ans += len(sticker)
            for s in sticker:
                board[ok_i + s[0]][ok_j + s[1]] = True
            break
        if tryy < 3:
            turn(h, w, sticker)
            h, w = w, h
print(ans)
