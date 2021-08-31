import sys
inputs = sys.stdin.readlines()

n = int(inputs[0])
board = [[0 for _ in range(n)]for _ in range(n)]

sd = dict()
sn = n*n
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
for c in range(sn):
    tmp = list(map(int, inputs[c+1].rstrip().split()))
    sd.setdefault(tmp[0], {tmp[1], tmp[2], tmp[3], tmp[4]})

    ii = 0
    jj = 0
    friend_cnt = -1
    empty_cnt = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                fc = 0
                ec = 0
                for dd in d:
                    ni = i+dd[0]
                    nj = j+dd[1]
                    if 0 <= ni < n and 0 <= nj < n:
                        if board[ni][nj] == 0:
                            ec += 1
                        elif board[ni][nj] in sd[tmp[0]]:
                            fc += 1
                if fc > friend_cnt:
                    friend_cnt = fc
                    empty_cnt = ec
                    ii = i
                    jj = j
                elif fc == friend_cnt and ec > empty_cnt:
                    friend_cnt = fc
                    empty_cnt = ec
                    ii = i
                    jj = j
    board[ii][jj] = tmp[0]

p = [0, 1, 10, 100, 1000]
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dd in d:
            ni = i+dd[0]
            nj = j+dd[1]
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] in sd[board[i][j]]:
                cnt += 1
        ans += p[cnt]
print(ans)
