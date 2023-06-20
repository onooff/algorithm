w, h = map(int, input().split())
board = list()
start = None
for i in range(h):
    board.append(input())
    if start == None:
        for j in range(w):
            if board[i][j] != '*' and board[i][j] != '.':
                start = (i, j)
                break

d = ((1, 0), (-1, 0), (0, 1), (0, -1))
q = [start]
cnt = 0
visited = {start}
tmp_visited = set()
dir_dict = {start: {0, 2}}
tmp_dir_dict = dict()
ans = -1

while len(q) > 0 and ans == -1:
    for v in q:
        y = v[0]
        x = v[1]
        if (0 in dir_dict[v]) or (1 in dir_dict[v]):
            for ndir in [2, 3]:
                if ans != -1:
                    break
                nd = d[ndir]
                ny = y
                nx = x
                while True:
                    ny += nd[0]
                    nx += nd[1]
                    nv = (ny, nx)
                    if not (0 <= ny < h and 0 <= nx < w and nv not in visited and board[ny][nx] != '*'):
                        break
                    if board[ny][nx] != '.':
                        ans = cnt
                        break
                    tmp_visited.add(nv)
                    tmp_dir_dict.setdefault(nv, set())
                    tmp_dir_dict[nv].add(ndir)

        if (2 in dir_dict[v]) or (3 in dir_dict[v]):
            for ndir in [0, 1]:
                if ans != -1:
                    break
                nd = d[ndir]
                ny = y
                nx = x
                while True:
                    ny += nd[0]
                    nx += nd[1]
                    nv = (ny, nx)
                    if not (0 <= ny < h and 0 <= nx < w and nv not in visited and board[ny][nx] != '*'):
                        break
                    if board[ny][nx] != '.':
                        ans = cnt
                        break
                    tmp_visited.add(nv)
                    tmp_dir_dict.setdefault(nv, set())
                    tmp_dir_dict[nv].add(ndir)

    if ans != -1:
        break

    cnt += 1
    q = list(tmp_dir_dict.keys())
    visited = visited | tmp_visited
    tmp_visited = set()
    dir_dict = tmp_dir_dict
    tmp_dir_dict = dict()

print(ans)
