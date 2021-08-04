'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''


def isin(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())

board = list()
ice_set = set()

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] > 0:
            ice_set.add((i, j))

keep_going = True
ans = 0
while keep_going and len(ice_set) > 0:
    ans += 1
    melt_set = set()
    for ice in ice_set:
        melt = 0
        for dd in d:
            ny = ice[0]+dd[0]
            nx = ice[1]+dd[1]
            if not isin(ny, nx, n, m) or board[ny][nx] <= 0:
                melt += 1
        if melt > 0:
            melt_set.add((ice[0], ice[1], melt))
    chk_bfs = False
    for melt in melt_set:
        board[melt[0]][melt[1]] -= melt[2]
        if board[melt[0]][melt[1]] <= 0:
            board[melt[0]][melt[1]] = 0
            ice_set.discard((melt[0], melt[1]))
            chk_bfs = True
    if len(ice_set) == 0:
        keep_going = False
        break
    if chk_bfs:
        mass_set = set()
        start = list(ice_set)[0]
        q = [start]
        mass_set.add(start)
        while len(q) > 0:
            now = q.pop(0)
            for dd in d:
                ny = now[0]+dd[0]
                nx = now[1]+dd[1]
                if (ny, nx) in ice_set and (ny, nx) not in mass_set:
                    q.append((ny, nx))
                    mass_set.add((ny, nx))
        if len(mass_set) != len(ice_set):
            # print(len(mass_set), len(ice_set))
            keep_going = False
if len(ice_set) == 0:
    print(0)
else:
    print(ans)
