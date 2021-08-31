def isin(y, x, size):
    return 0 <= y < size and 0 <= x < size


def set_to_tuple(set_type_yx):
    l = list(set_type_yx)
    if l[0][0] == l[1][0]:
        if l[0][1] < l[1][1]:
            return((l[0], l[1]))
        else:
            return((l[1], l[0]))
    else:
        if l[0][0] < l[1][0]:
            return((l[0], l[1]))
        else:
            return((l[1], l[0]))


def solution(board):
    size = len(board)
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    chk = {((0, 0), (0, 1))}
    q = [{(0, 0), (0, 1)}]
    nq = list()
    time = 0
    while True:
        cur = q.pop(0)
        ##############이동####################
        for dd in d:
            new = set()
            for yx in cur:
                ny = yx[0]+dd[0]
                nx = yx[1]+dd[1]
                if isin(ny, nx, size) and board[ny][nx] == 0:
                    new.add((ny, nx))
                else:
                    break
            if len(new) == 2:
                if (size-1, size-1) in new:
                    return time+1
                new = set_to_tuple(new)
                if new not in chk:
                    chk.add(new)
                    nq.append(new)
        ################회전###################
        cur = list(cur)
        p1 = cur[0]
        p2 = cur[1]
        rotate = (0, 1)
        if p1[0] == p2[0]:
            rotate = (2, 3)
        for go in range(2):
            for r in rotate:
                test1 = (p1[0]+d[r][0], p1[1]+d[r][1])
                test2 = (p2[0]+d[r][0], p2[1]+d[r][1])
                if isin(test1[0], test1[1], size) and isin(test2[0], test2[1], size) and board[test1[0]][test1[1]] == 0 and board[test2[0]][test2[1]] == 0:
                    new = {p1, test1}
                    # print("??", new, cur, rotate)
                    if (size-1, size-1) in new:
                        return time+1
                    new = set_to_tuple(new)
                    if new not in chk:
                        chk.add(new)
                        nq.append(new)
            p1, p2 = p2, p1
        # print(cur, time, len(q), nq)
        if len(q) == 0:
            time += 1
            q = nq
            nq = list()
    return time


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
