def solution(grid):
    h = len(grid)
    w = len(grid[0])
    d = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상우하좌
    chk = [[[False for _ in range(w)]for _ in range(h)]for _ in range(4)]

    answer = list()
    for i in range(h):
        for j in range(w):
            for go in range(4):
                if not chk[go][i][j]:
                    ni = i
                    nj = j
                    nd = go
                    cnt = 0
                    # print(nd, ni, nj)
                    while not chk[nd][ni][nj]:
                        cnt += 1
                        chk[nd][ni][nj] = True
                        ni += d[nd][0]
                        nj += d[nd][1]
                        if ni < 0:
                            ni = h-1
                        elif ni >= h:
                            ni = 0
                        if nj < 0:
                            nj = w-1
                        elif nj >= w:
                            nj = 0

                        if grid[ni][nj] == 'L':
                            nd -= 1
                        elif grid[ni][nj] == 'R':
                            nd += 1

                        if nd < 0:
                            nd = 3
                        elif nd >= 4:
                            nd = 0
                        # print(nd, ni, nj)
                    answer.append(cnt)
                    # print(">>>", cnt)
    answer.sort()
    return answer
