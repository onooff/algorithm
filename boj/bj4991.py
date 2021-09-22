import sys
import copy
inputs = sys.stdin.readlines()

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
inf = 9999999999999


def dfs(graph, cur, chk, cost, minn):
    if len(chk) <= 0:
        minn[0] = min(cost, minn[0])
        return

    for nxt in graph[cur]:
        if nxt in chk and cost+graph[cur][nxt] < minn[0]:
            chk.discard(nxt)
            dfs(graph, nxt, chk, cost+graph[cur][nxt], minn)
            chk.add(nxt)


idx = -1
while True:
    idx += 1
    w, h = map(int, inputs[idx].rstrip().split())
    if w == 0 and h == 0:
        break

    board = list()
    chk = [[False for _ in range(w)] for _ in range(h)]
    start = None
    graph = dict()
    for i in range(h):
        idx += 1
        board.append(inputs[idx].rstrip())
        for j in range(w):
            if board[i][j] == 'x':
                chk[i][j] = True
            elif board[i][j] == 'o':
                start = (i, j)
                graph.setdefault((i, j), dict())
            elif board[i][j] == '*':
                graph.setdefault((i, j), dict())

    ans = 0
    for v in graph:
        chk_tmp = copy.deepcopy(chk)
        chk_tmp[v[0]][v[1]] = True
        q = [(v[0], v[1], 0)]
        q_idx = 0
        while q_idx < len(q):
            cur = q[q_idx]
            q_idx += 1
            for nd in d:
                ny = cur[0]+nd[0]
                nx = cur[1]+nd[1]
                if 0 <= ny < h and 0 <= nx < w and not chk_tmp[ny][nx]:
                    chk_tmp[ny][nx] = True
                    q.append((ny, nx, cur[2]+1))
                    if board[ny][nx] != '.':
                        graph[v].setdefault((ny, nx), cur[2]+1)

        if len(graph[v]) < len(graph)-1:
            ans = -1
            break

    if ans == -1:
        print(ans)
        continue

    minn = [inf]
    chk = set(graph.keys())
    chk.discard(start)
    dfs(graph, start, chk, 0, minn)
    ans = minn[0]

    print(ans)
