'''
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
'''


def solution(board):
    inf = 999999
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    size = len(board)
    need = dict()
    chk = set()
    blocks = dict()
    blocks_r = dict()
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0 and (i, j) not in chk:
                num = board[i][j]
                blocks.setdefault(num, set())
                miny = inf
                minx = inf
                maxy = -1
                maxx = -1
                tmp = (i, j)
                q = [tmp]
                chk.add(tmp)
                blocks[num].add(tmp)
                miny = min(miny, i)
                minx = min(minx, j)
                maxy = max(maxy, i)
                maxx = max(maxx, j)
                while len(q) > 0:
                    tmp = q.pop(0)
                    for dd in d:
                        ny = tmp[0]+dd[0]
                        nx = tmp[1]+dd[1]
                        new = (ny, nx)
                        if (0 <= ny < size and 0 <= nx < size) and new not in chk and board[ny][nx] == num:
                            q.append(new)
                            chk.add(new)
                            blocks[num].add(new)
                            miny = min(miny, ny)
                            minx = min(minx, nx)
                            maxy = max(maxy, ny)
                            maxx = max(maxx, nx)
                blocks_r.setdefault(num, (miny, minx, maxy+1, maxx+1))
                for a in range(miny, maxy+1):
                    for b in range(minx, maxx+1):
                        new = (a, b)
                        if new not in blocks[num]:
                            need.setdefault(new, set())
                            need[new].add(num)
    base = [size-1 for _ in range(size)]
    for j in range(size):
        for i in range(size):
            if board[i][j] == 0:
                base[j] = i
            else:
                break
    # print(blocks)
    # print(need)
    # print(base)

    answer = 0
    go = True
    l = [i for i in range(size)]
    while go:
        go = False
        chk = set()
        nl = set()
        for j in l:
            i = base[j]
            tmp = (i, j)
            if tmp in need:
                for block in need[tmp]:
                    blocks[block].add(tmp)
                    board[tmp[0]][tmp[1]] = inf
                    base[tmp[1]] -= 1
                    nl.add(tmp[1])
                    go = True

                    chk.add(block)
        for block in chk:
            if len(blocks[block]) >= 6:
                cells = blocks.pop(block)
                answer += 1
                for c in cells:
                    nl.add(c[1])
                    board[c[0]][c[1]] = 0
                    if c in need:
                        need[c].discard(block)
                        if len(need[c]) == 0:
                            need.pop(c)
        l = list(nl)
        for j in l:
            for i in range(size):
                if board[i][j] == 0:
                    base[j] = i
                else:
                    break
        # for i in range(size):
        #     print(board[i])
        # print(blocks)
        # print(l)
        # print("------------------------------------------")
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
      0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))


print(solution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 2, 2, 1, 3, 3, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
]))
