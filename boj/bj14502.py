import copy

n, m = map(int, input().split())
board = list()
chk = [[False for _ in range(m)] for _ in range(n)]
viruses = list()
safe_default = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            safe_default += 1
        else:
            chk[i][j] = True
            if board[i][j] == 2:
                viruses.append((i, j))

size = m*n
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
maxx = 0


def test(i, j, chk, board):
    if board[i][j] != 0:
        return False
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ni = i+di
            nj = j+dj
            if len(chk) <= ni or ni < 0 or len(chk[0]) <= nj or nj < 0 or chk[ni][nj]:
                return True
    return False


for a in range(size-2):
    if test(a//m, a % m, chk, board):
        chk[a//m][a % m] = True
        for b in range(a+1, size-1):
            if test(b//m, b % m, chk, board):
                chk[b//m][b % m] = True
                for c in range(b+1, size):
                    if test(c//m, c % m, chk, board):
                        chk[c//m][c % m] = True
                        # print(a//m, a % m, b//m, b % m, c//m, c % m)
                        q = copy.deepcopy(viruses)
                        idx = 0
                        safe = safe_default-3
                        chk_tmp = copy.deepcopy(chk)
                        while idx < len(q):
                            y = q[idx][0]
                            x = q[idx][1]
                            for nd in d:
                                ny = y+nd[0]
                                nx = x+nd[1]
                                if 0 <= ny < n and 0 <= nx < m and not chk_tmp[ny][nx]:
                                    chk_tmp[ny][nx] = True
                                    q.append((ny, nx))
                                    safe -= 1
                            idx += 1
                        # print(safe)
                        maxx = max(maxx, safe)

                        chk[c//m][c % m] = False
                chk[b//m][b % m] = False
        chk[a//m][a % m] = False

print(maxx)
