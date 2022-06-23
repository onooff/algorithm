h, w = map(int, input().split())
board = list()
for i in range(h):
    board.append(input())


def is_in(h, w, y, x):
    return 0 <= y < h and 0 <= x < w


d = ((1, 0), (-1, 0), (0, 1), (0, -1))
chk = [[False for _ in range(w)] for _ in range(h)]
ans = -1
for i in range(h):
    for j in range(w):
        if board[i][j] == 'W' or chk[i][j]:
            continue

        chk[i][j] = True
        q = [(i, j)]
        nq = list()
        idx = 0
        candidates = list()
        while idx < len(q):
            cur = q[idx]
            idx += 1
            is_c = True
            for nd in d:
                ny = cur[0]+nd[0]
                nx = cur[1]+nd[1]
                if is_in(h, w, ny, nx) and board[ny][nx] == 'L' and not chk[ny][nx]:
                    is_c = False
                    chk[ny][nx] = True
                    nq.append((ny, nx))
            if is_c:
                candidates.append(cur)
            if idx == len(q):
                q = nq
                nq = list()
                idx = 0
        for c in candidates:
            tmp_chk = {c}
            q = [c]
            nq = list()
            idx = 0
            cnt = 0
            while idx < len(q):
                cur = q[idx]
                idx += 1
                for nd in d:
                    ny = cur[0]+nd[0]
                    nx = cur[1]+nd[1]
                    tmp = (ny, nx)
                    if is_in(h, w, ny, nx) and board[ny][nx] == 'L' and tmp not in tmp_chk:
                        tmp_chk.add(tmp)
                        nq.append(tmp)
                if idx == len(q):
                    cnt += 1
                    q = nq
                    nq = list()
                    idx = 0
            ans = max(cnt, ans)
print(ans-1)
